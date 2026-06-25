const form = document.getElementById("loginForm");
const button = document.getElementById("loginButton");
const statusText = document.getElementById("status");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    button.disabled = true;
    statusText.textContent = "Signing in...";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            statusText.textContent = data.detail || "Login failed.";
            button.disabled = false;
            return;
        }

        localStorage.setItem("access_token", data.access_token);
        window.location.href = "/dashboard.html";

    } catch (err) {
        statusText.textContent = "Unable to reach server.";
        button.disabled = false;
    }
});