// sticky navbar

let navbar = $(".header");

$(window).scroll(() => {
    // let oTop = $(".section-2").offset().top - window.innerHeight;
    if ($(window).scrollTop() > 50) {
        navbar.addClass('sticky');
    } else {
        navbar.removeClass('sticky');
    }
});

// Counter section
let nCount = selector => {
    $(selector).each(function () {
        $(this)
            .animate({
                Counter: $(this).text()
            }, {
                    duration: 4000,
                    easing: "swing",
            
                    step: function (value) {
                        $(this).text(Math.ceil(value));
                    }
                });
    });
};

let a = 0;
$(window).scroll(function () {
    // The .offset() method allows us to retrieve the current position of an element  relative to the document
  let oTop = $(".stats").offset().top - window.innerHeight;
    if (a == 0 && $(window).scrollTop() >= oTop) {
        a++;
      nCount(".stats-box > h3");
    }
});


   