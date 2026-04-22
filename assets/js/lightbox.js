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
    '<button class="lightbox-close" aria-label="Close">&times;</button><div class="lightbox-stage"></div>';
  document.body.appendChild(overlay);

  const stage = overlay.querySelector(".lightbox-stage");
  const closeBtn = overlay.querySelector(".lightbox-close");

  function openOne(src, alt) {
    stage.className = "lightbox-stage";
    stage.innerHTML = "";
    const img = document.createElement("img");
    img.src = src;
    img.alt = alt || "";
    stage.appendChild(img);
    show();
  }

  function openPair(figures) {
    stage.className = "lightbox-stage pair";
    stage.innerHTML = "";
    figures.forEach((fig) => {
      const srcImg = fig.querySelector("img");
      if (!srcImg) return;
      const wrap = document.createElement("figure");
      const img = document.createElement("img");
      img.src = srcImg.currentSrc || srcImg.src;
      img.alt = srcImg.alt || "";
      wrap.appendChild(img);
      const capEl = fig.querySelector("figcaption");
      if (capEl) {
        const cap = document.createElement("figcaption");
        cap.textContent = capEl.textContent;
        wrap.appendChild(cap);
      }
      stage.appendChild(wrap);
    });
    show();
  }

  function show() {
    overlay.classList.add("open");
    document.documentElement.style.overflow = "hidden";
  }

  function close() {
    overlay.classList.remove("open");
    document.documentElement.style.overflow = "";
    setTimeout(() => {
      stage.innerHTML = "";
      stage.className = "lightbox-stage";
    }, 200);
  }

  overlay.addEventListener("click", (e) => {
    if (e.target.closest("figure") && e.target.tagName !== "FIGCAPTION") return;
    if (e.target === overlay || e.target === closeBtn || e.target === stage) close();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });

  document.addEventListener("click", (e) => {
    const target = e.target.closest(SELECTORS.join(","));
    if (!target) return;
    if (target.closest("a")) return;

    const pairParent = target.closest(".hero-pair");
    if (pairParent) {
      const figs = Array.from(pairParent.querySelectorAll("figure"));
      if (figs.length) {
        e.preventDefault();
        openPair(figs);
        return;
      }
    }

    const img = target.tagName === "IMG" ? target : target.querySelector("img");
    if (!img) return;
    e.preventDefault();
    openOne(img.currentSrc || img.src, img.alt);
  });
})();
