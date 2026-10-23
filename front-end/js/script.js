const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const currentYear = document.querySelector("#current-year");

if (currentYear) {
    currentYear.textContent = new Date().getFullYear();
}

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
        const isExpanded =
            menuToggle.getAttribute("aria-expanded") === "true";

        menuToggle.setAttribute("aria-expanded", String(!isExpanded));
        navLinks.classList.toggle("is-open", !isExpanded);
    });

    navLinks.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        });
    });
}