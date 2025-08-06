// -------------------------------
// SECTION 1: Live Time Updater
// -
function updateTime() {
    const now = new Date();
    const formatted = now.toLocaleString('en-US', {
        month: 'long',
        day: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
    });
    document.getElementById("live-time").textContent = formatted;
}

updateTime(); // set immediately
setInterval(updateTime, 60000); // update every 60 seconds

// -------------------------------
// SECTION 2: Anchor Link Click Scroll and Highlight
// ---
const ignoredIds = ['header']; // Add any IDs to ignore
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {

        const targetId = this.getAttribute('href').substring(1);

        // Check if this ID should be ignored
        if (ignoredIds.includes(targetId)) return;

        e.preventDefault();

        const target = document.getElementById(targetId);

        if (target) {
            // Remove highlight from all sections first
            document.querySelectorAll('.highlighted').forEach(el => {
                el.classList.remove('highlighted');
            });

            // Scroll to the target
            target.scrollIntoView({behavior: 'smooth', block: 'center'});

            // Add highlight
            target.classList.add('highlighted');

            // Remove highlight after 2 seconds
            //setTimeout(() => {
            //    target.classList.remove('highlighted');
            //}, 2000);
        }
    });
});

// -------------------------------
// SECTION 3: Scroll Animation Trigger using Intersection Observer
//
document.addEventListener("DOMContentLoaded", () => {
    const animatedElements = document.querySelectorAll(".scroll-animate-up, .scroll-animate-down, .scroll-animate-left");

    const observerOptions = {
        threshold: 0.2,
        rootMargin: "0px 0px -10px 0px"
    };

    const observer = new IntersectionObserver((entries, observer) => {
        let delay = 0;

        entries
            .filter(entry => entry.isIntersecting)
            .forEach((entry, index) => {
                const element = entry.target;

                // Apply staggered delay
                setTimeout(() => {
                    element.classList.add("active");
                }, delay);

                delay += 150; // Add 150ms delay between items
                observer.unobserve(element); // Animate only once
            });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));
});

// -------------------------------
// SECTION 4: SECTION 4: POP-UP MODAL HANDLER
//
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("customModal");       // Modal wrapper
    const modalBody = document.getElementById("modalBody");     // Container for dynamic content
    const closeModal = document.getElementById("closeModalBtn"); // "X" close button

    // Attach click listener to all buttons that trigger the modal
    document.querySelectorAll('.open-modal').forEach(button => {
        button.addEventListener("click", function (e) {
            e.preventDefault();

            const page = this.getAttribute("data-page"); // e.g. 'opd-channeling.html'

            // Load modal body content from server
            fetch(`modal-content/${page}`)
                .then(response => {
                    if (!response.ok) throw new Error("Page not found");
                    return response.text();
                })
                .then(html => {
                    modalBody.innerHTML = "";
                    modalBody.innerHTML = html;      // Inject content
                    modal.style.display = "block";   // Show modal


                    // 🔁 Restart animation on every open
                    const content = modal.querySelector(".modal-content");
                    content.scrollTop = 0; // 👈 Reset scroll position to top
                    content.style.animation = "none";
                    content.offsetHeight; // force reflow
                    content.style.animation = null;

                    observeModalAnimations(); // 👈 Hook in scroll-based animations
                })
                .catch(err => {
                    modalBody.innerHTML = "<p>Error loading content.</p>";
                    modal.style.display = "block";
                });
        });
    });

    // Close modal when "X" is clicked
    closeModal.onclick = function () {
        modal.style.display = "none";
    };

    // Close modal when clicking outside modal content
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    function observeModalAnimations() {
        const animatedItems = modal.querySelectorAll(
            ".scroll-animate-up, .scroll-animate-down, .scroll-animate-left"
        );

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: modal.querySelector(".modal-content"),
            threshold: 0.1
        });

        animatedItems.forEach(item => observer.observe(item));
    }
});

// document.addEventListener("DOMContentLoaded", function () {
//   const modal = document.getElementById("customModal");
//   const modalBody = document.getElementById("modalBody");
//   const closeModal = document.getElementById("closeModalBtn");
//
//   function openModalWithPage(pageUrl) {
//     // Show modal
//     modal.style.display = "block";
//
//     // Load content
//     fetch(pageUrl)
//       .then(response => response.text())
//       .then(html => {
//         modalBody.innerHTML = html;
//       })
//       .catch(error => {
//         modalBody.innerHTML = "<p>Error loading content.</p>";
//         console.error(error);
//       });
//   }
//
//   // Close modal button
//   closeModal.addEventListener("click", function () {
//     modal.style.display = "none";
//     modalBody.innerHTML = ""; // Clear content if needed
//   });
//
//   // Optional: Close when clicking outside
//   window.addEventListener("click", function (event) {
//     if (event.target === modal) {
//       modal.style.display = "none";
//       modalBody.innerHTML = "";
//     }
//   });
//
//   // Trigger auto modal on page load
//   openModalWithPage("modal-content/melioraa.html");
// });


