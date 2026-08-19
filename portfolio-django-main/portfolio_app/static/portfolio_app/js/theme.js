document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    const root = document.documentElement;

    if (!themeToggle) return;

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        root.classList.add("dark");
    }

    updateIcon();

    themeToggle.addEventListener("click", () => {
        root.classList.toggle("dark");

        const isDark = root.classList.contains("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");

        updateIcon();
    });

    function updateIcon() {
        const isDark = root.classList.contains("dark");

        themeToggle.textContent = isDark ? "☀️" : "🌙";
        themeToggle.setAttribute(
            "aria-label",
            isDark ? "Switch to light mode" : "Switch to dark mode"
        );
    }
});
