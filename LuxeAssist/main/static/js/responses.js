function getBotResponse(input) {
    //
    const name = request.user.first_name
    if (input == "Can I select only the services I want?") {
        return "Yes";
    } else if (input == "Will the price change?") {
        return "hello I'm  Thank you for contacting us! I appreciate your patience in waiting for answers to your questions and I will be happy to help you answer them via WhatsApp or call.Thank you.(name)";
    } else if (input == "Thank you") {
        return "welcome";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello, thank you for registering with us on our website (Luxe Assist). We are very happy to have you join us and look forward to providing you with the best service";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}