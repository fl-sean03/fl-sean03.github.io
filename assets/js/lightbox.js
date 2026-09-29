// Click an image to see it larger. Images that carry data-full open in an overlay;
// a pair of hero images opens side by side. Without this script the page still works.
(function () {
  "use strict";

  var SELECTOR = ".hero-pair img[data-full], .featured img[data-full], .prose img[data-full]";
  var images = Array.prototype.slice.call(document.querySelectorAll(SELECTOR));
  if (!images.length) return;

  var overlay = document.createElement("div");
  overlay.className = "lightbox";
  overlay.hidden = true;
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.setAttribute("aria-label", "Enlarged image");
  overlay.innerHTML =
    '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>' +
    '<div class="lightbox-stage"></div>';
  document.body.appendChild(overlay);

  var stage = overlay.querySelector(".lightbox-stage");
  var closeButton = overlay.querySelector(".lightbox-close");
  var opener = null;

  function figureFor(img, group) {
    var figure = document.createElement("figure");
    var copy = document.createElement("img");
    copy.src = img.getAttribute("data-full");
    copy.alt = img.alt;
    figure.appendChild(copy);
    var source = img.closest("figure");
    var caption = source && source.querySelector("figcaption");
    if (caption && group) {
      var text = document.createElement("figcaption");
      text.textContent = caption.textContent;
      figure.appendChild(text);
    }
    return figure;
  }

  function open(img) {
    var pair = img.closest(".hero-pair");
    var group = pair ? Array.prototype.slice.call(pair.querySelectorAll("img[data-full]")) : [img];
    stage.innerHTML = "";
    stage.className = "lightbox-stage" + (group.length > 1 ? " pair" : "");
    group.forEach(function (item) {
      stage.appendChild(figureFor(item, group.length > 1));
    });
    opener = img;
    overlay.hidden = false;
    document.documentElement.classList.add("lightbox-open");
    closeButton.focus();
  }

  function close() {
    if (overlay.hidden) return;
    overlay.hidden = true;
    stage.innerHTML = "";
    document.documentElement.classList.remove("lightbox-open");
    if (opener) opener.focus();
  }

  images.forEach(function (img) {
    img.setAttribute("tabindex", "0");
    img.setAttribute("role", "button");
    img.setAttribute("aria-label", "View larger" + (img.alt ? ": " + img.alt : ""));
    img.addEventListener("click", function () {
      open(img);
    });
    img.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        open(img);
      }
    });
  });

  overlay.addEventListener("click", function (event) {
    if (event.target === overlay || event.target === stage || event.target === closeButton) close();
  });

  document.addEventListener("keydown", function (event) {
    if (overlay.hidden) return;
    if (event.key === "Escape") {
      close();
    } else if (event.key === "Tab") {
      // The close button is the only control, so focus stays on it.
      event.preventDefault();
      closeButton.focus();
    }
  });
})();
