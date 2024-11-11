// document.addEventListener("DOMContentLoaded", () => {
//     // Toggle navigation menu on smaller screens
//     const navToggle = document.createElement("button");
//     navToggle.className = "nav-toggle";
//     navToggle.innerText = "Menu";
//     document.querySelector("header").appendChild(navToggle);
  
//     const navMenu = document.querySelector("nav ul");
//     navToggle.addEventListener("click", () => {
//       navMenu.classList.toggle("visible");
//     });
  
//     // Smooth scrolling for internal links
//     const links = document.querySelectorAll('a[href^="#"], a[href^="index.html#"]');
//     links.forEach(link => {
//       link.addEventListener("click", function (e) {
//         e.preventDefault();
//         const target = document.querySelector(this.hash);
//         if (target) {
//           target.scrollIntoView({ behavior: "smooth" });
//         }
//       });
//     });
  
//     // Scroll-to-top button
//     const scrollToTopBtn = document.createElement("button");
//     scrollToTopBtn.className = "scroll-to-top";
//     scrollToTopBtn.innerText = "↑ Top";
//     document.body.appendChild(scrollToTopBtn);
  
//     window.addEventListener("scroll", () => {
//       if (window.pageYOffset > 300) {
//         scrollToTopBtn.style.display = "block";
//       } else {
//         scrollToTopBtn.style.display = "none";
//       }
//     });
  
//     scrollToTopBtn.addEventListener("click", () => {
//       window.scrollTo({ top: 0, behavior: "smooth" });
//     });
//   });
  