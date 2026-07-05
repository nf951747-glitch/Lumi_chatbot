window.addEventListener("load", function () {
    setTimeout(function () {
        document.getElementById("loading-screen").style.display = "none";
        document.getElementById("app").style.display = "flex";
        showWelcomeMessage();
    }, 2200);
});

function showWelcomeMessage() {
    setTimeout(function () {
        appendBotMessage("Heyy! I'm Lumi! ✨ Your cute little AI assistant! How can I help you today? 💜");
    }, 400);
}

function appendBotMessage(text) {
    var chatWindow = document.getElementById("chat-window");

    var wrapper = document.createElement("div");
    wrapper.classList.add("message", "bot");

    var avatar = document.createElement("div");
    avatar.classList.add("bot-avatar");
    avatar.innerHTML = '<img src="/static/images/lumi_robot.png" alt="Lumi" style="width:46px; height:46px; object-fit:cover; object-position: center top; border-radius:50%; border: 2px solid #D4C5F9; box-shadow: 0 2px 8px rgba(155,127,212,0.3);"/>';

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.textContent = text;

    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    chatWindow.appendChild(wrapper);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function appendUserMessage(text) {
    var chatWindow = document.getElementById("chat-window");

    var wrapper = document.createElement("div");
    wrapper.classList.add("message", "user");

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.textContent = text;

    wrapper.appendChild(bubble);
    chatWindow.appendChild(wrapper);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function showTyping() {
    var chatWindow = document.getElementById("chat-window");

    var indicator = document.createElement("div");
    indicator.classList.add("typing-indicator");
    indicator.id = "typing-indicator";

    var avatar = document.createElement("div");
    avatar.classList.add("bot-avatar");
    avatar.innerHTML = '<img src="/static/images/lumi_robot.png" alt="Lumi" style="width:46px; height:46px; object-fit:cover; object-position: center top; border-radius:50%; border: 2px solid #D4C5F9; box-shadow: 0 2px 8px rgba(155,127,212,0.3);"/>';

    var bubble = document.createElement("div");
    bubble.classList.add("typing-bubble");
    bubble.innerHTML = "<span></span><span></span><span></span>";

    indicator.appendChild(avatar);
    indicator.appendChild(bubble);
    chatWindow.appendChild(indicator);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function hideTyping() {
    var indicator = document.getElementById("typing-indicator");
    if (indicator) {
        indicator.remove();
    }
}

function sendMessage() {
    var input = document.getElementById("user-input");
    var text = input.value.trim();

    if (!text) return;

    input.value = "";
    appendUserMessage(text);
    showTyping();

    document.getElementById("send-btn").disabled = true;

    var delay = Math.floor(Math.random() * 600) + 600;

    setTimeout(function () {
        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        })
        .then(function (res) { return res.json(); })
        .then(function (data) {
            hideTyping();
            appendBotMessage(data.response);
            document.getElementById("send-btn").disabled = false;

            if (data.exit) {
                setTimeout(function () {
                    document.getElementById("farewell-overlay").style.display = "flex";
                }, 1000);
            }
        })
        .catch(function () {
            hideTyping();
            appendBotMessage("Oops! Something went wrong on my end! 🌿 Try again?");
            document.getElementById("send-btn").disabled = false;
        });
    }, delay);
}

function sendQuick(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}

function restartChat() {
    document.getElementById("farewell-overlay").style.display = "none";
    var chatWindow = document.getElementById("chat-window");
    chatWindow.innerHTML = "";
    showWelcomeMessage();
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("user-input").addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
});