function fireKamehameha() {
    const button = document.getElementById("attack-btn");
    const targetText = document.getElementById("doomed-text");
    const gif = document.getElementById("goku-gif");

    // 1. Trigger the HTTP Request for the GIF!
    console.log("1. Requesting GIF from server... (Check your Network tab!)");
    gif.src = "https://media.tenor.com/zOzUxL-uF_0AAAAi/future-alec-alec.gif"; 
    gif.style.display = "block";

    // Update button text and disable it so they can't click it twice
    button.innerText = "KAA... MEE... HAA... MEE...";
    button.disabled = true;

    // 2. Make the text react to the charging power
    targetText.classList.add("shake");
    targetText.innerText = "Uh oh... what is happening?! AHHHHH!";
    console.log("2. Energy level increasing...");

    // 3. Set a timer for 3 seconds (3000 milliseconds) for the blast!
    setTimeout(() => {
        
        console.log("3. KAMEHAMEHA FIRED!");
        button.innerText = "HAAAAAAAAA! 💥";
        
        // Change the text to an explosion
        targetText.innerText = "💥 POOF! 💥";
        targetText.style.color = "red";
        targetText.classList.remove("shake");

        // 4. Set another timer to actually delete it from the page
        setTimeout(() => {
            targetText.style.opacity = "0"; // Fade out
            console.log("4. Target successfully obliterated. 404 Text Not Found.");
            
            // Wait for fade out, then remove from DOM completely
            setTimeout(() => targetText.remove(), 500); 
            
        }, 1000);

    }, 3000); // Wait 3 seconds before firing
}