let aboutNav = document.getElementById('nav-about');
let homeNav = document.getElementById('nav-home');
let sermonNav = document.getElementById('nav-sermon');
let announcementsNav = document.getElementById('nav-announcements');
let contactNav = document.getElementById('nav-contact');
let galleryNav = document.getElementById('nav-gallery');
let fellowshipNav = document.getElementById('nav-fellowship');
let prayerNav = document.getElementById('nav-prayer');
let testimoneyNav = document.getElementById('nav-testimoney');
let eventsNav = document.getElementById('nav-events');


if (window.location.pathname == '/') {
    homeNav.className = 'active';
} else if(window.location.pathname == '/about/') {
    aboutNav.className = 'active';
    // console.log('true')
} else if (window.location.pathname == '/sermons/') {
    sermonNav.className = 'active';
} else if (window.location.pathname == '/announcements/') {
    announcementsNav.className = 'active';
} else if (window.location.pathname == '/gallery/'){
    galleryNav.className = 'active';
} else if (window.location.pathname == '/satelite-fellowship-centers/'){
    fellowshipNav.className = 'active';
} else if (window.location.pathname == '/prayer-request/'){
    prayerNav.className = 'active';
} else if (window.location.pathname == '/testimoney/'){
    testimoneyNav.className = 'active';
} else if (window.location.pathname == '/events/'){
    eventsNav.className = 'active';
} else if (window.location.pathname == '/contact/'){
    contactNav.className = 'active';
}
