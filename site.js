document.documentElement.classList.add("js");

addEventListener("DOMContentLoaded", () => {
  const seen = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("in");
      seen.unobserve(entry.target);
    });
  }, { threshold: 0.06 });
  document.querySelectorAll(".reveal").forEach((node) => seen.observe(node));

  // Il video parte solo quando si vede: pesa 10 MB.
  document.querySelectorAll("video[data-lazy]").forEach((video) => {
    new IntersectionObserver(([entry], watcher) => {
      if (!entry.isIntersecting) return;
      video.src = video.dataset.lazy;
      video.play().catch(() => {});
      watcher.disconnect();
    }, { rootMargin: "300px" }).observe(video);
  });

  // Anteprima: né la handlekurv né i moduli fanno davvero qualcosa.
  // Menu a tutto schermo
  const burger = document.querySelector(".burger");
  const menu = document.querySelector(".menu");
  const toggle = (open) => {
    menu.classList.toggle("open", open);
    menu.inert = !open;
    burger.setAttribute("aria-expanded", String(open));
    document.documentElement.classList.toggle("menu-open", open);
  };
  burger.addEventListener("click", () => toggle(!menu.classList.contains("open")));
  menu.addEventListener("click", (event) => { if (event.target.closest("a")) toggle(false); });
  addEventListener("keydown", (event) => { if (event.key === "Escape") toggle(false); });
  // Tornando indietro con il browser il menu non deve restare aperto.
  addEventListener("pageshow", () => toggle(false));

  const toast = document.querySelector(".toast");
  let timer;
  const say = (text) => {
    toast.textContent = text;
    toast.classList.add("show");
    clearTimeout(timer);
    timer = setTimeout(() => toast.classList.remove("show"), 3200);
  };
  document.querySelectorAll("[data-demo]").forEach((button) => {
    button.addEventListener("click", () => say(button.dataset.demo));
  });
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      form.querySelector(".form-note").textContent = document.body.dataset.formDemo;
    });
  }
});
