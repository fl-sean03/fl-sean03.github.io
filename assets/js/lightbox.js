(function () {
  const SELECTORS = [
    ".hero-pair figure",
    "figure.featured-image",
    ".article-content p > img",
    ".article-content > img",
  ];

  const overlay = document.createElement("div");
  overlay.className = "lightbox-overlay";
  overlay.innerHTML =
    '<button class="lightbox-close" aria-label="Close">&times;</button><div class="lightbox-stage"><img alt=""></div>';
  document.body.appendChild(overlay);

  const stageImg = overlay.querySelector("img");
  const closeBtn = overlay.querySelector(".lightbox-close");

  function open(src, alt) {
    stageImg.src = src;
    stageImg.alt = alt || "";
    overlay.classList.add("open");
    document.documentElement.style.overflow = "hidden";
  }

  function close() {
    overlay.classList.remove("open");
    document.documentElement.style.overflow = "";
    setTimeout(() => {
      stageImg.src = "";
    }, 200);
  }

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay || e.target === closeBtn) close();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });

  document.addEventListener("click", (e) => {
    const target = e.target.closest(SELECTORS.join(","));
    if (!target) return;
    if (target.closest("a")) return;
    const img = target.tagName === "IMG" ? target : target.querySelector("img");
    if (!img) return;
    e.preventDefault();
    open(img.currentSrc || img.src, img.alt);
  });
})();
