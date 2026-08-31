document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("nav-button");
  const menu = document.getElementById("mobile-nav");
  const themeToggle = document.getElementById("themeToggle");
  const savedTheme = localStorage.getItem("portfolio-theme");

  if (savedTheme === "light") document.body.classList.add("light-mode");
  const updateIcon = () => { if (themeToggle) themeToggle.textContent = document.body.classList.contains("light-mode") ? "☀" : "☾"; };
  updateIcon();

  if (themeToggle) themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
    localStorage.setItem("portfolio-theme", document.body.classList.contains("light-mode") ? "light" : "dark");
    updateIcon();
  });

  if (button && menu) {
    button.addEventListener("click", () => menu.classList.toggle("open"));
    menu.querySelectorAll("a").forEach(a => a.addEventListener("click", () => menu.classList.remove("open")));
  }
});
