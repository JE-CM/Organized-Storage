
function changeContent() {
    const welcomeMessage = document.getElementById('welcome-message');
    welcomeMessage.innerText = "Entering site...";
    document.body.style.backgroundColor = '#f0f0f0';
    setTimeout(function() {
        window.location.href = '/login';  // Redirects the browser to /login after 250 ms second
    }, 250);
}
