// 1. This will show up in the browser's Developer Tools Console immediately
console.log("Hello from the DevContainer! The JavaScript file has loaded successfully.");

// 2. A simple function we can trigger from the HTML
function changeText() {
    const messageElement = document.getElementById("js-message");
    
    // Change the text and the color
    messageElement.innerText = "Wow! JavaScript just changed this text!";
    messageElement.style.color = "blue";
    
    // Log the action to the console
    console.log("The button was clicked and the text was updated.");
}