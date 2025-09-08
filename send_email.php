<?php
// --- CONFIGURATION ---
$recipient_email = "info@kimwanyidairyfarmers.org";
$subject = "New Contact Form Submission from KDFCSL Website";
// --- END CONFIGURATION ---

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and get form data
    $first_name = filter_var(trim($_POST["First-Name"]), FILTER_SANITIZE_STRING);
    $last_name = filter_var(trim($_POST["Last-Name"]), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST["Email"]), FILTER_SANITIZE_EMAIL);
    $phone = filter_var(trim($_POST["Phone"]), FILTER_SANITIZE_STRING);
    
    // Use the new descriptive names
    $area_of_support = isset($_POST["Area-of-Support"]) ? filter_var(trim($_POST["Area-of-Support"]), FILTER_SANITIZE_STRING) : "Not specified";
    $role_in_partnership = isset($_POST["Role-in-Partnership"]) ? filter_var(trim($_POST["Role-in-Partnership"]), FILTER_SANITIZE_STRING) : "Not specified";
    
    $message = filter_var(trim($_POST["Message"]), FILTER_SANITIZE_STRING);

    // Basic validation
    if (empty($first_name) || empty($last_name) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($message)) {
        http_response_code(400);
        echo "Please fill out all required fields.";
        exit;
    }

    // Build the email content with clear labels
    $email_content = "First Name: $first_name\n";
    $email_content .= "Last Name: $last_name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n\n";
    $email_content .= "Area of Support: $area_of_support\n";
    $email_content .= "Role in Partnership: $role_in_partnership\n\n";
    $email_content .= "Message:\n$message\n";

    // Build the email headers
    $email_headers = "From: $first_name $last_name <$email>";

    // Send the email
    if (mail($recipient_email, $subject, $email_content, $email_headers)) {
        http_response_code(200);
        echo "Thank You! Your message has been sent.";
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
    }

} else {
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>