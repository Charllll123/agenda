document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    const navRect = nav.getBoundingClientRect();

    const snow = new Snowfall({
        minSize: 10,
        maxSize: 30,
        type: "text",
        content: "&#10052",
        fadeOut: true,
        autoplay: true,
        interval: 200
    });

    // Ajusta la posición de los copos de nieve para que caigan solo dentro del área de la barra de navegación
    snow.snowAnimate = function() {
        const size = random(snow.options.minSize, snow.options.maxSize);
        const top = navRect.top - size;
        const left = random(navRect.left, navRect.right - size);
        const opacity = random(5, 10) / 10;
        const angle = random(null, winHeight * 0.8, 1);
        const translateX = random(-100, 100);
        const translateY = winHeight + size * 2;

        let snowflakeElement;

        if (snow.queue.length) {
            snowflakeElement = snow.queue.shift();
            if (snowflakeElement.dataset.type !== snow.options.type) {
                snowflakeElement = new Snowflake();
            }
        } else {
            snowflakeElement = new Snowflake();
        }

        const styleRules = {
            "top": top + "px",
            "left": left + "px",
            "opacity": opacity,
            "transform": "none",
            "transition": snow.options.interval + "ms linear"
        };

        switch (snow.options.type) {
            case "solid":
                styleRules.width = styleRules.height = size + "px";
                break;
            case "text":
                styleRules["font-size"] = size + "px";
                break;
            case "image":
                styleRules.width = size + "px";
                break;
        }

        setStyle(snowflakeElement, styleRules);
        snow.$snowfield.appendChild(snowflakeElement);

        setTimeout(function() {
            setStyle(snowflakeElement, {
                "transform": "translate(" + translateX + "px," + translateY + "px) rotate(" + angle + "deg)",
                "opacity": snow.options.fadeOut ? 0 : opacity
            });
        }, 100);
    };

    // Inicia el efecto de nieve
    snow.play();
});
