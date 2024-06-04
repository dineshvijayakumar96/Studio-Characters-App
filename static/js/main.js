// Text Animation Starts

// import { gsap } from "https://cdn.skypack.dev/gsap@3.11.4";
// import splitType from "https://cdn.skypack.dev/split-type@0.3.3";

// // Function to create the animation for a single element
// function createAnimation(element) {
//   const ourText = new splitType(element, { types: "chars" });
//   const chars = ourText.chars;

//   return gsap.fromTo(
//     chars,
//     {
//       y: 100,
//       opacity: 0,
//     },
//     {
//       y: 0,
//       opacity: 1,
//       stagger: 0.05,
//       duration: 1,
//       ease: "power1.out",
//     }
//   );
// }

// // Function to check if an element is in the viewport
// function isElementInViewport(element) {
//   const rect = element.getBoundingClientRect();
//   return (
//     rect.top >= 0 &&
//     rect.left >= 0 &&
//     rect.bottom <=
//       (window.innerHeight || document.documentElement.clientHeight) &&
//     rect.right <= (window.innerWidth || document.documentElement.clientWidth)
//   );
// }

// // Function to handle the scroll event
// function handleScroll() {
//   const elements = document.querySelectorAll(".text-animate");
//   elements.forEach((element) => {
//     if (isElementInViewport(element)) {
//       if (!element.hasAttribute("data-animated")) {
//         const animation = createAnimation(element);
//         animation.play();
//         element.setAttribute("data-animated", "true");
//       }
//     } else {
//       // Reset the 'data-animated' attribute when the element is not in the viewport
//       element.removeAttribute("data-animated");
//     }
//   });
// }

// // Create an Intersection Observer
// const observertext = new IntersectionObserver((entries) => {
//   entries.forEach((entry) => {
//     if (entry.isIntersecting) {
//       const animation = createAnimation(entry.target);
//       animation.play();
//       observertext.unobserve(entry.target);
//     }
//   });
// });

// // Add elements to the observer
// const elements = document.querySelectorAll(".text-animate");
// elements.forEach((element) => {
//   observertext.observe(element);
// });

// // Listen for scroll events to handle initial animations
// window.addEventListener("scroll", handleScroll);

// Text Animation Ends

gsap.registerPlugin(ScrollTrigger);

gsap.defaults({ lazy: false });

gsap.to(".slide-1-1", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  // rotation: 45,
  scale: 17,
  duration: 2,
  force3D: false,
  ease: "power4.out",
});

gsap.to(".slide-1-2", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  rotation: 45,
  scale: 17,
  duration: 2,
  force3D: false,
  ease: "power4.out",
});

gsap.to(".slide-1-3", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  rotation: -45,
  scale: 17,
  duration: 2,
  force3D: false,
  ease: "power4.out",
});

gsap.to(".slide-1-4", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  rotation: 45,
  scale: 17,
  duration: 2,
  force3D: false,
  ease: "power4.out",
});

gsap.to(".slide-1-5", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  rotation: -45,
  scale: 17,
  duration: 2,
  force3D: false,
  ease: "power4.out",
});

ScrollTrigger.create({
  trigger: "#slide-1-reveal",
  start: "top top",
  end: "+=199%",
  scrub: 1,
  pin: true,
  pinSpacing: false,

  // markers: true,
});

// gsap.to("#slide-1-reveal", {
//   scrollTrigger: {
//     trigger: ".slide-1-frame",
//     start: "bottom bottom", // Adjust for mobile
//     end: "+=199%", // Adjust for mobile
//     scrub: 1,
//     // toggleActions: "play none none reverse",
//     markers: true,
//   },
//   clipPath: 'circle(100%)',
//   duration: 2,
//   force3D: false,
//   ease: "power4.out",
// });

gsap.to("#slide-1-reveal", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "+=250%", // Adjust for mobile
    scrub: 4,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  clipPath: 'circle(100%)',
  duration: 1,
  force3D: false,
  ease: "power4.out",
});

gsap.to("#slide-1-reveal", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "70% 70%", // Adjust for mobile
    end: "80% 80%", // Adjust for mobile
    scrub: 1,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  opacity: 0,
  force3D: false,
  ease: "power4.out",
});

// Background
gsap.to(".slide-1-5-1", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "10% 10%", // Adjust for mobile
    end: "bottom bottom", // Adjust for mobile
    scrub: 2,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  scale: 17,
  borderRadius: 0,
  duration: 1,
});

// gsap.to(".slide-1-5-1", {
//   scrollTrigger: {
//     trigger: ".slide-1-frame",
//     start: "center center-=100px", // Adjust for mobile
//     end: "center center-=100px", // Adjust for mobile
//     scrub: 2,
//     // toggleActions: "play none none reverse",
//     // markers: true,
//   },
//   // opacity: 1,
//   duration: 1,
// });

// gsap.to(".slide-1-5-1", {
//   scrollTrigger: {
//     trigger: ".slide-1",
//     start: "bottom bottom", // Adjust for mobile
//     end: "+=150%", // Adjust for mobile
//     scrub: 2,
//     // toggleActions: "play none none reverse",
//     // markers: true,
//   },
//   yPercent: -1100,
//   // duration: 1,
// });

// gsap.to(".slide-1-group", {
//   scrollTrigger: {
//     trigger: ".slide-1",
//     start: "bottom bottom", // Adjust for mobile
//     end: "+=150%", // Adjust for mobile
//     scrub: 1,
//     pinSpacing: false,
//     // toggleActions: "play none none reverse",
//     // markers: true,
//   },
//   opacity: 0,
//   // duration: 1,
// });

// Slide 1 Ends //////////////////////////////////////////////////////

// Text
gsap.to(".slide-1-7", {
  scrollTrigger: {
    trigger: ".slide-1-frame",
    start: "center center-=100px", // Adjust for mobile
    end: "center center-=100px", // Adjust for mobile
    scrub: 2,
    // toggleActions: "play none none reverse",
    // markers: true,
  },
  display: "flex",
  opacity: 1,
  duration: 1,
});

// Logo
// gsap.to(".slide-1-7", {
//   scrollTrigger: {
//     trigger: ".slide-1-frame",
//     toggleClass: "reveal-text",
//     start: "center center-=100px", // Adjust for mobile
//     end: "bottom bottom", // Adjust for mobile
//     scrub: 2,
//     // toggleActions: "play none none reverse",
//     // markers: true,
//   },
//   // rotation: -45,
//   // scale: 1.5,
//   duration: 1,
//   ease: "power4.out",
// });

// Service Section
// gsap.from("#service-1", {
//   xPercent: -90,
// });
gsap.to("#service-1", {
  scrollTrigger: {
    trigger: "#main-service",
    start: "50% 50%",
    end: "+=110%",
    scrub: 1,
    // toggleActions: "play none none reverse",

    // markers: true,
  },
  // rotation: -45,
  // scale: 1,
  xPercent: 90,
  // duration: 1,
  // ease: "power1.out",
});

// gsap.from("#service-2", {
//   xPercent: 90,
// });
gsap.to("#service-2", {
  scrollTrigger: {
    trigger: "#main-service",
    start: "50% 50%",
    end: "+=110%",
    scrub: 1,
    // toggleActions: "play none none reverse",

    // markers: true,
  },
  // rotation: -45,
  // scale: 1,
  xPercent: -90,
  // duration: 1,
  // ease: "power1.out",
});

// gsap.from("#service-spliter", {
//     yPercent: 700,
// });
gsap.to("#service-spliter", {
  scrollTrigger: {
    trigger: "#main-service",
    start: "50% 50%",
    end: "+=110%",
    scrub: 1,
    // toggleActions: "play none none reverse",

    // markers: true,
  },
  // rotation: -45,
  // scale: 1,
  yPercent: -1000,
  // duration: 1,
  // ease: "power1.out",
});

gsap.to("#service-img", {
  scrollTrigger: {
    trigger: "#main-service",
    start: "bottom bottom",
    end: "+=110%",
    scrub: 1,
    // snap: true,
    // toggleActions: "play none none reverse",
    // pin: "#main-service",

    // pinSpacing: false,
    // markers: true,
  },
  scale: 1,
});

ScrollTrigger.create({
  trigger: "#main-service",
  start: "bottom bottom",
  end: "+=150%",
  scrub: 1,
  pin: true,
  // pinSpacing: false,
  // markers: true,
});

// var tlService = gsap.timeline({scrollTrigger:{
//     trigger:"#main-service",
//     start:"50% 50%",
//     end:"+=150%",
//     scrub:true,
//     snap: true,
//     pin:'#main-service',
//     // pinSpacing: false,
//     // markers: true,
// }});
// tlService
// .to("#service-img", {
//     scale: 1,
// });

// gsap.to(".slide-1-group", {
//     scrollTrigger: {
//         trigger: ".slide-1-frame",
//         start: "10% 10%", // Adjust for mobile
//         end: "bottom bottom", // Adjust for mobile
//         scrub: 2,
//         // toggleActions: "play none none reverse",
//         // markers: true,
//     },
//     scale: 4,
//     duration: 1,
//     ease: "power4.out",
// });

// Slide 3
// var tl = gsap.timeline({scrollTrigger:{
//     trigger:"#main",
//     // markers:true,
//     start:"50% 50%",
//     end:"150% 50%",
//     scrub:2,
//     pin:true,
// }});
// tl
// .to("#slide-3-port-2",{
//     yPercent: -100,
//  },'a')
//  .to("#slide-3-port-3",{
//     yPercent: -200,
//  },'a');

// Section 3 Portfolio
gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

gsap.utils.toArray(".panel2").forEach((panel2, i) => {
  let trigger = ScrollTrigger.create({
    trigger: panel2,
    start: "top top",
    scrub: 1,
    pin: true,
    pinSpacing: false,
  });
});

ScrollTrigger.create({
  trigger: "#one",
  start: "top top",
  end: "+=700%",
  scrub: 1,
  pin: true,
  pinSpacing: false,
  // markers: true,
});

gsap.from("#two", {
  scale: 1,
});
gsap.to("#two", {
  scrollTrigger: {
    trigger: "#two",
    start: "bottom bottom",
    end: "+=80%",
    pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  scale: 0.5,
});
gsap.to("#two", {
  scrollTrigger: {
    trigger: "#two",
    start: "+=5%",
    end: "+=10%",
    pinSpacing: false,
    scrub: true,

    // markers: true,
  },
  opacity: 0,
});

gsap.from("#three", {
  scale: 1,
});
gsap.to("#three", {
  scrollTrigger: {
    trigger: "#three",
    start: "bottom bottom",
    end: "+=80%",
    // pin: true,
    pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  scale: 0.5,
});
gsap.to("#three", {
  scrollTrigger: {
    trigger: "#three",
    start: "+=5%",
    end: "+=10%",
    pinSpacing: false,
    scrub: true,

    // markers: true,
  },
  opacity: 0,
});

gsap.from("#four", {
  scale: 1,
});
gsap.to("#four", {
  scrollTrigger: {
    trigger: "#four",
    start: "bottom bottom",
    end: "+=80%",
    // pin: true,
    pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  scale: 0.5,
});
gsap.to("#four", {
  scrollTrigger: {
    trigger: "#four",
    start: "+=5%",
    end: "+=10%",
    pinSpacing: false,
    scrub: true,

    // markers: true,
  },
  opacity: 0,
});

gsap.from("#five", {
  scale: 1,
});
gsap.to("#five", {
  scrollTrigger: {
    trigger: "#five",
    start: "bottom bottom",
    end: "+=80%",
    // pin: true,
    pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  scale: 0.5,
});
gsap.to("#five", {
  scrollTrigger: {
    trigger: "#five",
    start: "+=5%",
    end: "+=10%",
    pinSpacing: false,
    scrub: true,

    // markers: true,
  },
  opacity: 0,
});

gsap.from("#six", {
  scale: 1,
});
gsap.to("#six", {
  scrollTrigger: {
    trigger: "#six",
    start: "bottom bottom",
    end: "+=80%",
    // pin: true,
    pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  scale: 0.5,
});
gsap.to("#six", {
  scrollTrigger: {
    trigger: "#six",
    start: "+=5%",
    end: "+=10%",
    pinSpacing: false,
    scrub: true,

    // markers: true,
  },
  opacity: 0,
});

// Section 4
ScrollTrigger.create({
  trigger: "#section-4-panel",
  start: "top top",
  end: "+=200%",
  scrub: 1,
  pin: true,
  pinSpacing: false,

  // markers: true,
});

// gsap.from("#section-4-panel-2-2", {
//   scale: 0,
// });
gsap.to("#section-4-panel-2-2", {
  scrollTrigger: {
    trigger: "#section-4-panel-2",
    start: "bottom bottom",
    end: "+=150%",
    pin: true,
    // pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  clipPath: 'circle(100%)',
});

gsap.to("#section-4-panel-3-card-1", {
  scrollTrigger: {
    trigger: "#section-4-panel-3",
    start: "center center",
    end: "+=150%",
    pin: true,
    // pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  xPercent: 150,
});

gsap.to("#section-4-panel-3-card-3", {
  scrollTrigger: {
    trigger: "#section-4-panel-3",
    start: "center center",
    end: "+=150%",
    // pin: true,
    // pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  xPercent: -150,
});

gsap.to("#section-4-panel-3-card-2", {
  scrollTrigger: {
    trigger: "#section-4-panel-3",
    start: "center center",
    end: "+=150%",
    // pin: true,
    // pinSpacing: false,
    snap: false,
    scrub: 1,

    // markers: true,
  },
  opacity: 1,
});

gsap.to("#section-4-panel-3-card-4", {
  scrollTrigger: {
    trigger: "#section-4-panel-3",
    start: "bottom 60%",
    end: "bottom bottom",
    // pin: true,
    // pinSpacing: false,
    snap: false,
    scrub: 1,

    // markers: true,
  },
  opacity: 1,
});

// gsap.from("#section-4-text-1", {
//     xPercent: -150,
// });
// gsap.to("#section-4-text-1", {
//     scrollTrigger: {
//         trigger: "#section-4-panel-3",
//         start: "center center",
//         end: "+=150%",
//         pin: true,
//         // pinSpacing: false,
//         scrub: 1,
//         // markers: true,
//     },
//     xPercent: 150,
// });

// gsap.to("#section-4-text-2", {
//     scrollTrigger: {
//         trigger: "#section-4-panel-3",
//         start: "center center",
//         end: "+=150%",
//         // pin: true,
//         // pinSpacing: false,
//         scrub: 1,
//         // markers: true,
//     },
//     xPercent: -150,
// });

// Section 6-5
ScrollTrigger.create({
  trigger: "#section-6-main",
  start: "top top",
  end: "+=100%",
  scrub: 1,
  pin: true,
  pinSpacing: false,

  // markers: true,
});

ScrollTrigger.create({
  trigger: "#section-6-panel-1",
  start: "top top",
  end: "bottom bottom",
  scrub: 1,
  pin: true,

  pinSpacing: false,
  // markers: true,
});

// gsap.from("#section-6-sub-panel-1", {
//     opacity: 0,
// });
gsap.to("#section-6-sub-panel-1", {
  scrollTrigger: {
    trigger: "#section-6-panel-1",
    start: "top top",
    end: "+=199%",
    // pin: true,
    // pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  opacity: 1,
});
gsap.to("#a", {
  scrollTrigger: {
    trigger: "#section-6-panel-1",
    start: "top top",
    end: "+=100%",
    // pin: true,
    // pinSpacing: false,
    scrub: 1,

    // markers: true,
  },
  rotation: 90,
});

// Portfolio Single Page
ScrollTrigger.create({
  trigger: "#portfolio-1-main-1",
  start: "top top",
  end: "bottom bottom",
  pin: "#portfolio-1-section-1",
  pinSpacing: false,
  scrub: 1,

  // markers: true,
});

let portfolioImages = gsap.utils.toArray(
  "#portfolio-1-section-2 .portfolio-1-section-2-imgs"
);

portfolioImages.forEach((image) => {
  gsap.to(image, {
    scrollTrigger: {
      trigger: image,
      start: "top 100%",
      // end: "top 80%",
      // pin: true,
      // pinSpacing: false,
      // scrub: 1,
      toggleActions: "play none none reverse",

      // markers: true,
    },
    yPercent: -10,
    duration: 1,
    // ease: "power1.out",
  });
});

// ScrollTO Functions
// Ensure GSAP and ScrollToPlugin are available
gsap.registerPlugin(ScrollToPlugin);

// Handle the click event
document.addEventListener('DOMContentLoaded', function () {
    document
    .getElementById("scrollto-main-service")
    .addEventListener("click", function () {
        gsap.to(window, {
        scrollTo: "#main-service",
        duration: 1,
        ease: "power2.inOut",
        });
    });

    document
    .getElementById("scrollto-section-3-main")
    .addEventListener("click", function () {
        gsap.to(window, {
        scrollTo: "#section-3-main",
        duration: 1,
        ease: "power2.inOut",
        });
    });

    document
    .getElementById("scrollto-section-4-main")
    .addEventListener("click", function () {
        gsap.to(window, {
        scrollTo: "#section-4-main",
        duration: 1,
        ease: "power2.inOut",
        });
    });

    document
    .getElementById("scrollto-section-6-main")
    .addEventListener("click", function () {
        gsap.to(window, {
        scrollTo: "#section-6-main",
        duration: 1,
        ease: "power2.inOut",
        });
    });

    document
    .getElementById("scrollto-footer-enquiry")
    .addEventListener("click", function () {
        gsap.to(window, {
        scrollTo: "#footer-enquiry",
        duration: 1,
        ease: "power2.inOut",
        });
    });
  });

  // Whole Website for Smooth Scroll
  

// Navbar Mobile Menu Animation
// gsap.to("#m-navbar-menu-1", {
//     scrollTrigger: {
//         trigger: "#m-navbar-menu-1",
//         start: "top center",
//         end: "top center",
//         // pin: true,
//         // pinSpacing: false,
//         // scrub: true,
//         toggleActions: "play none none reverse",
//         markers: true,
//     },
//     top: 0,
// });

//const div = document.querySelectorAll('div');
//const divArr = Array.prototype.slice.call(div);

// gsap.utils.toArray("#opennav").forEach((el, i) => {
//     const tl = gsap.timeline({
//         paused: true,
//         reversed: true
//     });

//     tl.to(el, {
//         top: '0%',
//         duration: 1
//     });

//     const menuElements = document.querySelectorAll(".m-navbar-menu");

//     el.addEventListener('click', function () {
//         tl.restart(); // Restart the timeline from the beginning

//         gsap.to(menuElements, {
//             top: '0%',
//             delay: 1,
//             duration: 1,
//             stagger: 0.1 // Optional: stagger the animations for each element
//         });
//     });
// });

// Section 5
// ScrollTrigger.create({
//     trigger: "#section-5-panel-1",
//     start: "top top",
//     end: "+=200%",
//     scrub: 1,
//     pin: true,
//     pinSpacing: false,
//     markers: true,
// });

// gsap.from("#section-5-panel-2", {
//     scale: 0,
// });
// gsap.to("#section-5-panel-2", {
//     scrollTrigger: {
//         trigger: "#section-5-panel-1",
//         start: "top top",
//         end: "+=100%",
//         // pin: true,
//         // pinSpacing: false,
//         scrub: 1,
//         // markers: true,
//     },
//     scale: 1,
// });

// Mobile Navbar
// document.addEventListener('DOMContentLoaded', function () {
//     // Toggle mobile menu visibility
//     document.getElementById('mobile-menu-btn').addEventListener('click', function () {
//         document.getElementById('mobile-menu').classList.toggle('hidden');
//     });

//     // Close mobile menu on close button click
//     document.getElementById('mobile-menu-close-btn').addEventListener('click', function () {
//         document.getElementById('mobile-menu').classList.add('hidden');
//     });
// });

// Navbar Background Black
// document.addEventListener('DOMContentLoaded', function () {
//     window.addEventListener('load', () => {
//         const navbar = document.querySelector('.navbar-top');
//         const sections = document.querySelectorAll('.bg-white, .bg-black');

//         const observer = new IntersectionObserver(entries => {
//           entries.forEach(entry => {
//             if (entry.target.classList.contains('bg-white') && entry.isIntersecting) {
//               navbar.classList.add('bg-black');
//             } else if (!entry.target.classList.contains('bg-white') && !entry.isIntersecting) {
//               navbar.classList.remove('bg-black');
//             }
//           });
//         }, { threshold: 0.5 });

//         sections.forEach(section => {
//           observer.observe(section);
//         });
//       });
// });

// Enquiry Form Animation
const form = document.querySelector(".footer-enquiry-form-fields");

// Select all input elements within the form
const inputFields = form.querySelectorAll(".footer-enquiry-form-input");

// Loop through each input field and add event listeners
inputFields.forEach((inputField) => {
  inputField.addEventListener("focus", () => {
    // Select the element with class .form-border-2 relative to the current input field
    const borderElement =
      inputField.parentElement.querySelector(".form-border-2");
    if (borderElement) {
      borderElement.classList.add("active-form-input");
    }
  });

  inputField.addEventListener("blur", () => {
    const borderElement =
      inputField.parentElement.querySelector(".form-border-2");
    if (borderElement) {
      borderElement.classList.remove("active-form-input");
    }
  });
});
// Enquiry Form Animation Ends

// Navbar
/********** Sidenav Open/Close **********/
// document.addEventListener('DOMContentLoaded', function () {
//     const openNavElement = document.getElementById('opennav');
//     const mySidenavElement = document.getElementById('mySidenav');

//     openNavElement.addEventListener('click', function () {
//         // Toggle the width of the navigation menu
//         mySidenavElement.style.width = (mySidenavElement.style.width === '100%') ? '0' : '100%';
//         mySidenavElement.style.opacity = (mySidenavElement.style.opacity === '1') ? '0' : '1';

//         // Toggle the active class for the burger button
//         openNavElement.classList.toggle('active');
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
  const openNavElement = document.getElementById("opennav");
  const mySidenavElement = document.getElementById("mySidenav");
  const menuElements = document.querySelectorAll(".m-navbar-menu");
  const menuAnchors = document.querySelectorAll(".navbar-nav a");

  const tl = gsap.timeline({ paused: true, reversed: true });
  tl.to(openNavElement, { top: "0%", duration: 1 });

  openNavElement.addEventListener("click", function () {
    toggleMenu();
  });

  menuAnchors.forEach((anchor) => {
    anchor.addEventListener("click", function () {
      toggleMenu();
    });
  });

  function toggleMenu() {
    // Toggle the width and opacity of the navigation menu
    mySidenavElement.style.width =
      mySidenavElement.style.width === "100%" ? "0" : "100%";
    mySidenavElement.style.opacity =
      mySidenavElement.style.opacity === "1" ? "0" : "1";

    // Toggle the active class for the burger button
    openNavElement.classList.toggle("active");

    // Toggle the animation for the m-navbar-menu elements
    if (openNavElement.classList.contains("active")) {
      tl.play();
      gsap.to(menuElements, {
        top: "0%",
        delay: 0.5,
        duration: 1,
        stagger: 0.1, // Optional: stagger the animations for each element
      });
    } else {
      tl.reverse();
      gsap.to(menuElements, {
        top: "110%",
        duration: 1,
      });
    }
  }
});

// Navbar Ends

// Service Page Website
document.addEventListener('DOMContentLoaded', function () {
  const serviceBtn = document.querySelector('.service-btn');
  const container = document.getElementById('service-website-1');

  document.addEventListener('mousemove', function (event) {
    const mouseX = event.clientX;
    const mouseY = event.clientY;

    // Center the serviceBtn to the mouse pointer
    const btnWidth = serviceBtn.offsetWidth;
    const btnHeight = serviceBtn.offsetHeight;
    const btnX = mouseX - btnWidth / 2;
    const btnY = mouseY - btnHeight / 2;

    const containerRect = container.getBoundingClientRect();

    // Check if the mouse coordinates are within the container's boundaries
    const withinXBounds = mouseX >= containerRect.left && mouseX <= containerRect.right;
    const withinYBounds = mouseY >= containerRect.top && mouseY <= containerRect.bottom;

    if (withinXBounds && withinYBounds) {
      // Inside the container, show the button and update its position
      serviceBtn.style.opacity = '1';
      serviceBtn.style.transition = 'transform 0.1s linear';
      serviceBtn.style.transform = `translate(${btnX}px, ${btnY}px)`;
    } else {
      // Outside the container, hide the button
      serviceBtn.style.opacity = '0';
      serviceBtn.style.transition = 'all 0.5s ease-in-out';
    }
  });
});
// Service Page Website Ends

// Scroll to functions
// document.addEventListener('DOMContentLoaded', function () {

//   let anchorClicked = false;

//   gsap.utils.toArray("#navigation-bar a").forEach(function (a) {
//     let wrap = document.querySelector("#scrollWrap"),
//       triggerEl = document.querySelector(a.getAttribute("href").substring(1)),
//       st = ScrollTrigger.create({
//         trigger: triggerEl,
//         pinnedContainer: wrap.contains(triggerEl) ? wrap : null,
//         start: "top 40"
//       });
//     a.addEventListener("click", function (e) {
//       anchorClicked = true;
//       e.preventDefault();
//       console.log("animate to", e.target.getAttribute("href"));
//       gsap.to(window, {
//         duration: 1,
//         scrollTo: {
//           y: st.start
//         },
//         onComplete: () => (anchorClicked = false)
//       });
//     });
//   });

// });
// Scroll to functions ends


// Initialize Swiper
// document.addEventListener('DOMContentLoaded', function () {
//   var swiper = new Swiper(".mySwiper", {
//     pagination: {
//       el: ".swiper-scrollbar",
//       hide: true,
//     },
//     slidesPerView: 1, // Number of slides per view
//     spaceBetween: 0, // Space between slides
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//   });
// });

// Service Portfolio Slider Starts
document.addEventListener('DOMContentLoaded', function () {
  // Get all elements with the class "characters-slider-img" and "characters-slider-content"
  var imgElements = document.querySelectorAll('.characters-slider-img');
  var contentElements = document.querySelectorAll('.characters-slider-content');
  var totalSlides = imgElements.length;
  var intervalId; // Variable to store the interval ID

  // Update slider active status and total count
  function updateSliderStatus() {
      var activeIndex = 0;
      imgElements.forEach(function (element, index) {
          if (element.classList.contains('characters-slider-img-active')) {
              activeIndex = index + 1; // Add 1 to index to match human counting
          }
      });
      document.getElementById('characters-slider-active').textContent = ('0' + activeIndex).slice(-2); // Pad with leading zero if needed
      document.getElementById('characters-slider-total').textContent = ('0' + totalSlides).slice(-2); // Pad with leading zero if needed
  }

  // Function to add and remove the active class to the specified element with a delay
  function addRemoveActiveClassWithDelay(elements, activeClass) {
      elements.forEach(function (element, index) {
          setTimeout(function () {
              // Remove active class from all elements
              elements.forEach(function (prevElement) {
                  prevElement.classList.remove(activeClass);
              });

              // Add active class to the current element
              element.classList.add(activeClass);

              // Update slider status
              updateSliderStatus();
          }, index * 5000); // 5000 milliseconds = 5 seconds
      });
  }

  // Function to start the slideshow
  function startSlideshow() {
      intervalId = setInterval(function () {
          // Find the index of the current active slide
          var activeIndex;
          imgElements.forEach(function (element, index) {
              if (element.classList.contains('characters-slider-img-active')) {
                  activeIndex = index;
              }
          });

          // Calculate the index of the next slide
          var nextIndex = (activeIndex + 1) % totalSlides;

          // Remove active class from all slides
          imgElements.forEach(function (element) {
              element.classList.remove('characters-slider-img-active');
          });

          // Add active class to the next slide
          imgElements[nextIndex].classList.add('characters-slider-img-active');

          // Add active class to the corresponding content slide
          contentElements.forEach(function (element, index) {
              if (index === nextIndex) {
                  element.classList.add('characters-slider-content-active');
              } else {
                  element.classList.remove('characters-slider-content-active');
              }
          });

          // Update slider status
          updateSliderStatus();
      }, 5000); // 5000 milliseconds = 5 seconds
  }

  // Start the slideshow initially
  startSlideshow();

  // Add event listener for the left navigation button
  document.getElementById('characters-slider-nav-left').addEventListener('click', function () {
      clearInterval(intervalId); // Clear the interval

      // Find the index of the current active slide
      var activeIndex;
      imgElements.forEach(function (element, index) {
          if (element.classList.contains('characters-slider-img-active')) {
              activeIndex = index;
          }
      });

      // Calculate the index of the previous slide
      var prevIndex = (activeIndex - 1 + totalSlides) % totalSlides;

      // Remove active class from all slides
      imgElements.forEach(function (element) {
          element.classList.remove('characters-slider-img-active');
      });

      // Add active class to the previous slide
      imgElements[prevIndex].classList.add('characters-slider-img-active');

      // Add active class to the corresponding content slide
      contentElements.forEach(function (element, index) {
          if (index === prevIndex) {
              element.classList.add('characters-slider-content-active');
          } else {
              element.classList.remove('characters-slider-content-active');
          }
      });

      // Update slider status
      updateSliderStatus();

      // Start the slideshow again
      startSlideshow();
  });

  // Add event listener for the right navigation button
  document.getElementById('characters-slider-nav-right').addEventListener('click', function () {
      clearInterval(intervalId); // Clear the interval

      // Find the index of the current active slide
      var activeIndex;
      imgElements.forEach(function (element, index) {
          if (element.classList.contains('characters-slider-img-active')) {
              activeIndex = index;
          }
      });

      // Calculate the index of the next slide
      var nextIndex = (activeIndex + 1) % totalSlides;

      // Remove active class from all slides
      imgElements.forEach(function (element) {
          element.classList.remove('characters-slider-img-active');
      });

      // Add active class to the next slide
      imgElements[nextIndex].classList.add('characters-slider-img-active');

      // Add active class to the corresponding content slide
      contentElements.forEach(function (element, index) {
          if (index === nextIndex) {
              element.classList.add('characters-slider-content-active');
          } else {
              element.classList.remove('characters-slider-content-active');
          }
      });

      // Update slider status
      updateSliderStatus();

      // Start the slideshow again
      startSlideshow();
  });
});

// Service Portfolio Slider Ends

// Service page Website Services
document.addEventListener('DOMContentLoaded', function () {
  let serviceContainer = document.querySelector(".service-container");
  let servicePanels = serviceContainer.querySelectorAll(".service-panel");

  gsap.to(servicePanels, {
    xPercent: -60 * (servicePanels.length - 1),
    ease: "none",
    scrollTrigger: {
      trigger: serviceContainer,
      // markers: true,
      pin: true,
      scrub: 1,
      // snap: 1 / (servicePanels.length - 1),
      end: "+=200%"
    }
  });
});
// Service page Website Services Ends () => "+=" + serviceContainer.offsetWidth


// Service page Website Services
document.addEventListener('DOMContentLoaded', function () {
  let serviceContainer2 = document.querySelector(".service-container-m");
  let servicePanels2 = serviceContainer2.querySelectorAll(".service-panel-m");

  gsap.to(servicePanels2, {
    xPercent: -110.9 * (servicePanels2.length - 1),
    ease: "none",
    scrollTrigger: {
      trigger: serviceContainer2,
      // markers: true,
      pin: true,
      scrub: 1,
      // snap: 1 / (servicePanels2.length - 1),
      end: () => "+=" + serviceContainer2.offsetWidth
    }
  });
});
// Service page Website Services Ends () => "+=" + serviceContainer.offsetWidth

// Service page Website Services
document.addEventListener('DOMContentLoaded', function () {
  let serviceContainer11 = document.querySelector(".service-container-2");
  let servicePanels11 = serviceContainer11.querySelectorAll(".service-panel-2");

  gsap.to(servicePanels11, {
    xPercent: -83 * (servicePanels11.length - 1),
    ease: "none",
    scrollTrigger: {
      trigger: serviceContainer11,
      // markers: true,
      pin: true,
      scrub: 1,
      // snap: 1 / (servicePanels11.length - 1),
      end: "+=300%"
    }
  });
});
// Service page Website Services Ends () => "+=" + serviceContainer.offsetWidth

// Service page Website Services
document.addEventListener('DOMContentLoaded', function () {
  let serviceContainer22 = document.querySelector(".service-container-2-m");
  let servicePanels22 = serviceContainer22.querySelectorAll(".service-panel-2-m");

  gsap.to(servicePanels22, {
    xPercent: -110.9 * (servicePanels22.length - 1),
    ease: "none",
    scrollTrigger: {
      trigger: serviceContainer22,
      // markers: true,
      pin: true,
      scrub: 1,
      // snap: 1 / (servicePanels2.length - 1),
      end: "+=300%"
    }
  });
});
// Service page Website Services Ends () => "+=" + serviceContainer.offsetWidth

// // Function to toggle the visibility and opacity of a Team description
document.addEventListener("DOMContentLoaded", function() {
  const buttons = document.querySelectorAll("[data-description], [data-closedescription]");

  buttons.forEach(button => {
      button.addEventListener("click", function() {
          const targetId = this.dataset.description || this.dataset.closedescription;
          const targetElement = document.querySelector(`.${targetId}`);

          if (targetElement) {
              if (this.dataset.description) {
                  // Show the target element
                  targetElement.classList.remove("hidden");
                  targetElement.classList.add("opacity-100");
                  targetElement.classList.remove("top-2");
                  targetElement.classList.add("top-0");
                  targetElement.classList.remove("h-0");
                  targetElement.classList.add("h-auto");
              } else if (this.dataset.closedescription) {
                  // Hide the target element
                  targetElement.classList.add("hidden");
                  targetElement.classList.remove("opacity-100");
                  targetElement.classList.add("top-2");
                  targetElement.classList.remove("top-0");
                  targetElement.classList.add("h-0");
                  targetElement.classList.remove("h-auto");
              }
          }
      });
  });
});