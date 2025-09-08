<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // --- RECIPIENT INFORMATION ---
    $to = "info@kimwanyidairyfarmers.org";

    // --- FORM DATA & SUBJECT ---
    $first_name = htmlspecialchars($_POST['First-Name']);
    $last_name = htmlspecialchars($_POST['Last-Name']);
    $subject = "New Partnership Inquiry from " . $first_name . " " . $last_name;

    // --- EMAIL HEADERS ---
    $from_name = "Kimwanyi Dairy Farmers";
    $from_email = "no-reply@kimwanyidairyfarmers.org";
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: " . $from_name . " <" . $from_email . ">" . "\r\n";
    $headers .= "Reply-To: " . htmlspecialchars($_POST['Email']) . "\r\n";

    // --- REMAINING FORM DATA ---
    $email = htmlspecialchars($_POST['Email']);
    $phone = htmlspecialchars($_POST['Phone']);
    $area_of_support = htmlspecialchars($_POST['Area-of-Support']);
    $role = htmlspecialchars($_POST['Role-in-Partnership']);
    $message_content = htmlspecialchars($_POST['Message']);

    // --- STYLED EMAIL BODY ---
    $body = '
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>' . $subject . '</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: #f4f4f4; font-family: Arial, sans-serif;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td style="padding: 20px 0;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse; background-color: #ffffff; border: 1px solid #cccccc;">
                        <tr>
                            <td align="center" style="padding: 40px 0; background-color: #00573d; color: #ffffff;">
                                <h1 style="margin: 0; font-size: 24px;">New Partnership Inquiry</h1>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 30px 40px;">
                                <h2 style="border-bottom: 1px solid #eeeeee; padding-bottom: 15px; margin-top: 0; color: #333333;">Submission Details</h2>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px;"><strong>Name:</strong> ' . $first_name . ' ' . $last_name . '</p>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px;"><strong>Email:</strong> ' . $email . '</p>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px;"><strong>Phone:</strong> ' . $phone . '</p>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px;"><strong>Area of Support:</strong> ' . $area_of_support . '</p>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px;"><strong>Role in Partnership:</strong> ' . $role . '</p>
                                <h2 style="border-bottom: 1px solid #eeeeee; padding-bottom: 15px; margin-top: 30px; color: #333333;">Message</h2>
                                <p style="margin: 15px 0; color: #555555; font-size: 16px; line-height: 1.5;">' . nl2br($message_content) . '</p>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" style="padding: 20px 0; background-color: #f4f4f4; color: #888888; font-size: 12px;">
                                This email was sent from the form on kimwanyidairyfarmers.org
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>';

    // --- SEND EMAIL ---
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200);
        echo "Thank you! Your message has been sent.";
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong, and we couldn't send your message.";
    }

} else {
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>