(function($) {

	"use strict";	

  


})(jQuery);






$(window).load(function () {
    blogisotope = function () {
        var e, t = $(".blog-masonry").width(),
            n = Math.floor(t);
        if ($(".blog-masonry").hasClass("masonry-true") === true) {
            n = Math.floor(t * .3033);
            e = Math.floor(t * .04);
            if ($(window).width() < 1023) {
                if ($(window).width() < 768) {
                    n = Math.floor(t * 1)
                } else {
                    n = Math.floor(t * .48)
                }
            } else {
                n = Math.floor(t * .3033)
            }
        }
        return e
    };
    var r = $(".blog-masonry");
    bloggingisotope = function () {
        r.isotope({
            itemSelector: ".post-masonry",
            animationEngine: "jquery",
            masonry: {
                gutterWidth: blogisotope()
            }
        })
    };
    bloggingisotope();
    $(window).smartresize(bloggingisotope)
})

// get all the stars
const one = document.getElementById('first')
const two  = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    for ( let i=0; i < children.length; i++){
        if(i <=size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}


const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
//            one.classList.add('checked')
//            two.classList.remove('checked')
//            three.classList.remove('checked')
//            four.classList.remove('checked')
//            five.classList.remove('checked')
            handleStarSelect(1)
            return
        }
    }
    switch(selection){
        case 'second': {
            handleStarSelect(2)
            return
        }
    }
    switch(selection){
        case 'third': {
            handleStarSelect(3)
            return
        }
    }
    switch(selection){
        case 'fourth': {
            handleStarSelect(4)
            return
        }
    }
    switch(selection){
        case 'fifth': {
            handleStarSelect(5)
            return
        }
    }
}

if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        alert('clicked')
    }))
}

