document.addEventListener("DOMContentLoaded", () => {

    const root = document.documentElement;
    const theme = document.getElementById("theme-toggle");
    const navigation = document.querySelector(".navigation");
    const navButton = document.getElementById("nav-button");

    function updateTheme() {
        theme.textContent =
            root.classList.contains("dark") ? "☀️" : "🌙";
    }

    if (localStorage.getItem("theme") === "dark")
        root.classList.add("dark");

    updateTheme();

    theme.addEventListener("click", () => {
        root.classList.toggle("dark");

        localStorage.setItem(
            "theme",
            root.classList.contains("dark") ? "dark" : "light"
        );

        updateTheme();
    });

    navButton.addEventListener("click", (e) => {
        e.stopPropagation();
        navigation.classList.toggle("open");
    });

    document.addEventListener("click", (e) => {
        if (!navigation.contains(e.target))
            navigation.classList.remove("open");
    });

    navigation.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            navigation.classList.remove("open");
        });
    });

});
