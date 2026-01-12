document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".django-message");

    messages.forEach(message => {
        setTimeout(() => {
            message.classList.add("show");
        }, 100);

        setTimeout(() => {
            message.classList.remove("show");
        }, 4000);
    });
});