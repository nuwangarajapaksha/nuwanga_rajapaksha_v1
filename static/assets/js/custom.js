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


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
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


