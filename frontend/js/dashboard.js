const token = localStorage.getItem("access_token");
if (!token) {
    window.location.href = "/login.html";
}

async function loadUser() {
    try {
        const response = await fetch("/api/me", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        if (!response.ok) {
            localStorage.removeItem("access_token");
            window.location.href = "/login.html";
            return;
        }

        const data = await response.json();
        document.getElementById("username").textContent = data.username;

    } catch (err) {
        console.error(err);
        localStorage.removeItem("access_token");
        window.location.href = "/login.html";
    }
}

document.getElementById("logoutBtn").addEventListener("click", () => {
    localStorage.removeItem("access_token");
    window.location.href = "/login.html";
});

loadUser();