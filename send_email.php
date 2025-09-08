<?php

// --- DEBUGGING SCRIPT ---
// This script will show us what the server is receiving.

// Set the content type to plain text for easy reading
header('Content-Type: text/plain');

// Check if it's a POST request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    echo "--- Form Data Received by Server ---\n\n";
    
    // Check if the POST data array is empty
    if (empty($_POST)) {
        echo "The server received no form data. This might be a server configuration issue.\n";
    } else {
        // Print out all the data the server received
        foreach ($_POST as $key => $value) {
            echo "Field Name: '" . htmlspecialchars($key) . "'\n";
            echo "Submitted Value: '" . htmlspecialchars($value) . "'\n\n";
        }
    }

} else {
    // If it's not a POST request
    http_response_code(403);
    echo "This script should only be accessed via a POST request from your form.";
}

?>