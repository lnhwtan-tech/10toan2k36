document.addEventListener("DOMContentLoaded", function() {
    // 1. Tự động thêm preloader vào đầu trang nếu chưa có trong HTML
    if (!document.getElementById("preloader")) {
        const preloaderHTML = `
            <div id="preloader">
                <div class="spinner"></div>
            </div>
        `;
        document.body.insertAdjacentHTML('afterbegin', preloaderHTML);
    }

    const preloader = document.getElementById("preloader");
    window.addEventListener("load", () => {
        setTimeout(() => {
            if (preloader) {
                preloader.classList.add("loaded");
            }
        }, 500);
    });

    // 2. Tự động áp dụng hiệu ứng trượt lên cho các thành phần nội dung
    const targetSelectors = 'main > *, .container > *, section, .card, .achievement-item, .member-card';
    const elementsToAnimate = document.querySelectorAll(targetSelectors);

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, { 
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px' 
    });

    elementsToAnimate.forEach(el => {
        if (!el.closest('header') && !el.closest('nav')) {
            el.classList.add("animate-on-scroll");
            observer.observe(el);
        }
    });
});