/* --------------------------------------------
  DOCUMENT.READY
--------------------------------------------- */
$(document).ready(function(){
  'use strict';
 
  /* --------------------------------------------
    SEARCH
  --------------------------------------------- */
	//if you change this breakpoint in the style.css file (or _layout.scss if you use SASS), don't forget to update this value as well
	var MqL = 1170;
	//move nav element position according to window width

	//open search form
	$('.cd-search-trigger').on('click', function(event){
		event.preventDefault();
		toggleSearch();
	});

	function toggleSearch(type) {
		if(type=="close") {
			//close serach 
			$('.cd-search').removeClass('is-visible');
			$('.cd-search-trigger').removeClass('search-is-visible');
			$('.cd-overlay').removeClass('search-is-visible');
		} else {
			//toggle search visibility
			$('.cd-search').toggleClass('is-visible');
			$('.cd-search-trigger').toggleClass('search-is-visible');
			$('.cd-overlay').toggleClass('search-is-visible');
			if(windowT.width() > MqL && $('.cd-search').hasClass('is-visible')) $('.cd-search').find('input[type="search"]').focus();
			($('.cd-search').hasClass('is-visible')) ? $('.cd-overlay').addClass('is-visible') : $('.cd-overlay').removeClass('is-visible') ;
		}
	}

  /* --------------------------------------------
    EQUAL HEIGHTS
  --------------------------------------------- */
  //init equal height
  //$('.equal-height').equalHeights();

  /* --------------------------------------------
    SCROLL TO TOP
  --------------------------------------------- */
	// hide #back-top first
	$("#back-top").hide();
			
	// fade in #back-top
	$(function () {
		windowT.scroll(function () {
			if ($(this).scrollTop() > 100) {
        $('#back-top').fadeIn();
			} else {
				$('#back-top').fadeOut();
			}
    });

    // scroll body to 0px on click
    $('#back-top a').click(function () {
      $('body,html').animate({
        scrollTop: 0
      }, 600);
      return false;
    });
  });
  
  /* --------------------------------------------
    TOGGLE
  --------------------------------------------- */
	$('.toggle-view-custom li').click(function () {

		var text = $(this).children('div.panel');

		if (text.is(':hidden')) {
			text.slideDown('10');
			$(this).children('.ui-accordion-header').addClass('ui-accordion-header-active');		
		} else {
			text.slideUp('10');
			$(this).children('.ui-accordion-header').removeClass('ui-accordion-header-active');		
		}

	});
 
  /* --------------------------------------------
    SMOOTH SCROLL TO 
  --------------------------------------------- */
  $('a.smooth-scroll[href^="#"]').on('click', function(event) {

    var target = $( $(this).attr('href') );

    if( target.length ) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 600);
    }

  });

  /* --------------------------------------------
    JS NOT FOR MOBILE (PARALLAX, OPACITY SCROLL)
  --------------------------------------------- */
  if( mobileDetect == false ) {
    /* --------------------------------------------
      OPACITY SCROLL
    --------------------------------------------- */
    if ( $('.opacity-scroll2').length ){  
      windowT.on('scroll', function() {
        $('.opacity-scroll2').css('opacity', function() {
          return 1 - ((windowT.scrollTop() / windowT.height())*1.5);
        });
      });
    };
    
    /* --------------------------------------------
      PARALLAX
    --------------------------------------------- */
    if ( $('.parallax-section').length ){
      $.stellar({
        horizontalScrolling: false,
      }); 
    }; 
  
  }//END JS NOT FOR MOBILE
  
	/* --------------------------------------------
    SKILL BAR ANIMATION
  --------------------------------------------- */
	$('.skillbar').appear(function(){  
		$('.skillbar').each(function(){
			$(this).find('.skillbar-bar').animate({
				width:$(this).attr('data-percent')
			},2000);
		});
	});

  /* --------------------------------------------
    BOOTSTRAP JS
  --------------------------------------------- */
  //TOOLOTIPS INITIALIZE
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	});

  //POPOVER INITIALIZE	
	$(function () {
	  $('[data-toggle="popover"]').popover()
	});  
    
  // ACCORDION
  var accordPanels = $(".accordion > dd").hide();
  
    accordPanels.first().slideDown("easeOutExpo");
    $(".accordion > dt > a").first().addClass("active");
    
    $(".accordion > dt > a").click(function(){
    
      var current = $(this).parent().next("dd");
      $(".accordion > dt > a").removeClass("active");
      $(this).addClass("active");
      accordPanels.not(current).slideUp("easeInExpo");
      $(this).parent().next().slideDown("easeOutExpo");
      
      return false;
            
  });
  
  // TOGGLE
  $(".toggle > dd").hide();
  
  $(".toggle > dt > a").click(function(){
  
      if ($(this).hasClass("active")) {
      
          $(this).parent().next().slideUp("easeOutExpo");
          $(this).removeClass("active");
          
      }
      else {
          var current = $(this).parent().next("dd");
          $(this).addClass("active");
          $(this).parent().next().slideDown("easeOutExpo");
      }
      
      return false;
  });
  
  /* --------------------------------------------
    FUNCTIONS
  --------------------------------------------- */
  initMenu();
  initMagnPopup();
  initCounters();
  initMap();
  initPageSliders();
  initImgHeight();
  initLeftMenu();
  if ( $('#flickr-feeds').length ){
    initFlickrFeeds();
  };
  if ( $('#twitter-feeds').length ){
    initTwitterFeeds();
  };
  if ( $('#nav').length ){
    initAffixCheck();
  };
  if ( $('#items-grid').length ){
    initWorkFilter();
  };
  if ( $('.masonry').length ){
    initMasonry();
  };
  if ( $('.wow').length ){
    initWow(); 
  };
  if ( $('#nav-stick2').length ){
    initNavStick2();
  };
  
  //WINDOW RESIZE
  windowT.resize(function() {
    //$('.equal-height').css('height','auto').equalHeights();
    if ( $('#nav').length ){
      initAffixCheck();
    };
    initImgHeight();
    initLeftMenu();
  }); 
  
  //WINDOW WIDTH CHANGE
  var widthWin = windowT.width();
  windowT.resize(function(){
     if($(this).width() != widthWin){
        widthWin = $(this).width();
        initLeftMenu();
     }
  });
  
});

/* --------------------------------------------
  HEADER MENU
--------------------------------------------- */
function initMenu() {
	'use strict';
  var $       = jQuery,
	  body    = $('body'),
	  primary = '#main-menu';
  
  $(primary).find('.parent > a .open-sub, .megamenu .title .open-sub').remove();
  
  $(primary).find('.parent > a, .megamenu .title').append('<span class="open-sub"></span>');
	  
  $(primary).on('click','.open-sub', function(event){	  
	event.preventDefault();
	
	var item = $(this).closest('li, .box');
	
	if ($(item).hasClass('active')) {
	  $(item).children().last().slideUp(150);
	  $(item).removeClass('active');
	} else {
	  var li = $(this).closest('li, .box').parent('ul, .sub-list').children('li, .box');
	  
	  if ($(li).is('.active')) {
		$(li).removeClass('active').children('ul').slideUp(150);
	  }
	  
	  $(item).children().last().slideDown(150);
	  $(item).addClass('active');
	}
  });

   $(primary).find('.parent > a').click(function(event){
	if ((body.width()  > 979) &&  (navigator.userAgent.match(/iPad|iPhone|Android/i))) {
	  var link = $(this);
	  
	  if (link.parent().hasClass('open')) {
		link.parent().removeClass('open'),
		event.preventDefault();
	  } else {
		event.preventDefault();
		link.parent().addClass('open')
	  }
	}
  }); 

}

/* --------------------------------------------
  PLATFORM DETECT
--------------------------------------------- */

var htmlT    = $('html'),
    windowT    = $(window),
    ieDetect = false,
    mobileDetect = false,
    ua = window.navigator.userAgent,
    old_ie = ua.indexOf('MSIE '),
    new_ie = ua.indexOf('Trident/');
  
  if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)) {
    mobileDetect = true;
    htmlT.addClass('mobile');
  } else {
    htmlT.addClass('no-mobile');
  };   
  
  //IE Detect
  if ((old_ie > -1) || (new_ie > -1)) {
    ieDetect = true;
  };
  
/* --------------------------------------------
  PAGE LOADER
--------------------------------------------- */
$("body").imagesLoaded(function(){
  $("#loader3").fadeOut();
  $("#loader-overflow").delay(200).fadeOut(700);
});

/* --------------------------------------------
  MAGNIFIC POPUP SETTINGS
--------------------------------------------- */
function initMagnPopup() {
	//Inline popups
		$('#inline-popups').magnificPopup({
		  delegate: 'a',
		  removalDelay: 500, //delay removal by X to allow out-animation
		  callbacks: {
			beforeOpen: function() {
			   this.st.mainClass = this.st.el.attr('data-effect');
			}
		  },
		  midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
		});

	//Image popups
		$('.lightbox').magnificPopup({
		 // delegate: 'a',
		  type: 'image',
		  mainClass: 'mfp-3d-unfold',
		  removalDelay: 500, //delay removal by X to allow out-animation
		  callbacks: {
			beforeOpen: function() {
			  // just a hack that adds mfp-anim class to markup 
			   this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
			  // this.st.mainClass = this.st.el.attr('data-effect');
			}
		  },
		  closeOnContentClick: true,
		  midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
		});

	//Hinge effect popup
		$('a.hinge').magnificPopup({
		  mainClass: 'mfp-with-fade',
		  removalDelay: 1000, //delay removal by X to allow out-animation
		  callbacks: {
			beforeClose: function() {
				this.content.addClass('hinge');
			}, 
			close: function() {
				this.content.removeClass('hinge'); 
			}
		  },
		  midClick: true
		});
		
	//GALERY
		$('.popup-gallery').magnificPopup({
			delegate: 'a',
			type: 'image',
			tLoading: 'Loading image #%curr%...',
			mainClass: 'mfp-3d-unfold',
		  removalDelay: 500, //delay removal by X to allow out-animation
		  callbacks: {
			beforeOpen: function() {
			  // just a hack that adds mfp-anim class to markup 
			   this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
			  // this.st.mainClass = this.st.el.attr('data-effect');
			}
		  },
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
				/*titleSrc: function(item) {
					return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
				}*/
			}
		});
	
	//GALERY 2
		$('.popup-gallery2').magnificPopup({
			delegate: 'a',
			type: 'image',
			tLoading: 'Loading image #%curr%...',
			mainClass: 'mfp-3d-unfold',
		  removalDelay: 500, //delay removal by X to allow out-animation
		  callbacks: {
			beforeOpen: function() {
			  // just a hack that adds mfp-anim class to markup 
			   this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
			  // this.st.mainClass = this.st.el.attr('data-effect');
			}
		  },
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
				/*titleSrc: function(item) {
					return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
				}*/
			}
		});
    
	//MULTI GALERY 
		$('.popup-multi-gallery').each(function() { // the containers for all your galleries
			$(this).magnificPopup({
				delegate: 'a', // the selector for gallery item
				type: 'image',
				tLoading: 'Loading image #%curr%...',
				mainClass: 'mfp-3d-unfold',
				removalDelay: 500, //delay removal by X to allow out-animation
				callbacks: {
					beforeOpen: function() {
						// just a hack that adds mfp-anim class to markup 
						 this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
						// this.st.mainClass = this.st.el.attr('data-effect');
					}
				},
				gallery: {
				  enabled:true,
					navigateByImgClick: true,
					preload: [0,1] // Will preload 0 - before current, and 1 after the current image
				},
				image: {
					tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
					/*titleSrc: function(item) {
						return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
					}*/
				}
			});
		});

	//VIDEO GMAPS POPUP
		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
			//disableOn: 700,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,

			fixedContentPos: false
		});
};	

/* --------------------------------------------
  FIXED HEADER ON - OFF
--------------------------------------------- */
function initAffixCheck(){
	'use strict';
  var navAffix = $('#nav');  
  
  //FIXED HEADER ON
  navAffix.affix({
    offset: { top: 1, }
  });
  
  if((windowT.width() < 1025) && (!$('#nav').hasClass('affix-on-mobile')) ) {
    //FIXED HEADER OFF
    windowT.off('.affix');
    navAffix.removeData('bs.affix').removeClass('affix affix-top affix-bottom');
  };
  
  if ($('#nav').hasClass('affix-on-mobile')) {
    $(".nav.navbar-nav").css("max-height", $(window).height() - $(".logo-row").height() - 20 + "px");
  }

}; 

/* --------------------------------------------
  TWITTER FEEDS
--------------------------------------------- */
function initTwitterFeeds(){
	$("#twitter-feeds").tweet({
    // join_text: false,
	  username: "abcgomel", // Change username here
	  modpath: './js/twitter/', // Twitter files path
	  avatar_size: false, // you can active avatar
	  count: 2, // number of tweets
	  loading_text: "loading tweets..."
	});
};   

/* --------------------------------------------
  FLICKR FEEDS
--------------------------------------------- */
function initFlickrFeeds(){					
  $('#flickr-feeds').jflickrfeed({
		limit: 6,
		qstrings: {
			id: '91212552@N07'
		},
		itemTemplate:
		'<li>' +
			'<a class="lightbox" rel="colorbox" href="{{image}}" title="{{title}}">' +
				'<img src="{{image_s}}" alt="{{title}}" />' +
			'</a>' +
		'</li>'
	});  
};          
            
/* --------------------------------------------
  HEADER LEFT MENU
--------------------------------------------- */
function initLeftMenu(){
  var hlNav = $('#header-left-nav');
  
  if((windowT.width() < 1025) ) {
    hlNav.removeClass('in')
  }
  if((windowT.width() > 1024) && (!hlNav.hasClass('in')) ) {
    hlNav.addClass('in')
  }

}; 

/* --------------------------------------------
  WOW ANIMATE
--------------------------------------------- */
function initWow(){
  var wow = new WOW( { mobile: false, } );
  wow.init();
}

/* ---------------------------------------------
  COUNTER
--------------------------------------------- */
function initCounters(){
  $(".count-number").appear(function(){
    var count = $(this);
    count.countTo({
      from: 0,
      to: count.html(),
      speed: 1300,
      refreshInterval: 60,
    });
  });
}

/* ---------------------------------------------
 PORTFOLIO
--------------------------------------------- */
function initWorkFilter(){
  // Projects filtering
  var fselector = 0,
      itemsGrid = $("#items-grid");
    
    (function($){
     "use strict";
     var isotopeMode;
     if (itemsGrid.hasClass("masonry")){
         isotopeMode = "masonry";
     } else{
         isotopeMode = "fitRows"
     }
     
     itemsGrid.imagesLoaded(function(){
            itemsGrid.isotope({
                itemSelector: '.mix',
                layoutMode: isotopeMode,
                filter: fselector
            });
        });
        
        $(".filter").click(function(){
            $(".filter").removeClass("active");
            $(this).addClass("active");
            fselector = $(this).attr('data-filter');
            
            itemsGrid.isotope({
                itemSelector: '.mix',
                layoutMode: isotopeMode,
                filter: fselector
            });
            return false;
        });
        
    })(jQuery);
}

/* ---------------------------------------------
 HEIGHT 100%  
 --------------------------------------------- */
function initImgHeight(){
  (function($){
    $(".js-height-fullscr").height($(window).height());
  })(jQuery);
} 

/* ---------------------------------------------
  MASONRY
--------------------------------------------- */
function initMasonry(){
  (function($){    
  
    $(".masonry").imagesLoaded(function(){
      $(".masonry").masonry();
    });
    
  })(jQuery);
}

/* ---------------------------------------------
 GOOGLE MAP
 --------------------------------------------- */
var gmMapDiv = $("#google-map");

function initMap(){
  (function($){
    
    if (gmMapDiv.length) {
  
      var gmCenterAddress = gmMapDiv.attr("data-address"),
          gmMarkerAddress = gmMapDiv.attr("data-address"),
          gmLat = gmMapDiv.attr("data-latitude"),
          gmLong = gmMapDiv.attr("data-longitude");
      
      gmMapDiv.gmap3({
          action: "init",
          marker: {
              //address: gmMarkerAddress,  //The option to specify the address instead of latitude and longitude. Read more in the documentation.
              latLng:[gmLat, gmLong], 
              options: {
                  icon: "images/loc-marker.png"
              }
          },
          map: {
              options: {
                  zoom: 18,
                  zoomControl: true,
                  zoomControlOptions: {
                      style: google.maps.ZoomControlStyle.SMALL
                  },
                  mapTypeControl: false,
                  scaleControl: false,
                  scrollwheel: false,
                  streetViewControl: false,
                  draggable: true,
                  styles:[ { stylers: [{ invert_lightness: true }, { saturation: -100 }, { lightness: 10 }] } ]
              }
          }
      });
    }
  })(jQuery);
}

/* --------------------------------------------
LOCAL HOSTED VIDEO PLAYER
-------------------------------------------- */	
	if ( $( ".date-picker" ).length !== 0 ) {
		$(function () {
			$('.date-picker').datetimepicker({
				format: 'DD/MM/YYYY'
			});
		});
	};	

	if ( $( ".time-picker" ).length !== 0 ) {
		$(function () {
			$('.time-picker').datetimepicker({
				format: 'LT'
			});
		});
	};	


/* ---------------------------------------------
 OWL Sliders 
 --------------------------------------------- */
function initPageSliders(){
    (function($){
        "use strict";
        
        // FULLWIDTH SLIDER
        $(".fullwidth-slider").owlCarousel({
            //rtl:true,
            slideSpeed: 350,
            singleItem: true,
           // autoHeight: true,
            navigation: true,
            navigationText: ["<span class='icon icon-arrows-left'></span>", "<i class='icon icon-arrows-right'></span>"]
        }); 

        // FULLWIDTH SLIDER AUTOPLAY
        $(".fullwidth-slider-auto").owlCarousel({
            autoPlay : 4000,
           // slideSpeed: 350,
            singleItem: true,
           // autoHeight: true,
            
            navigation: true,
            navigationText: ["<span class='icon icon-arrows-left'></span>", "<i class='icon icon-arrows-right'></span>"],
           // pagination : false,
            //paginationNumbers: false,
        });
       
        // CAROUSEL CLIENTS ITEMS
				$("#owl-clients").owlCarousel({
				  //Set AutoPlay to 3 seconds
				  autoPlay : 6000,
				  items : 5,
				  itemsDesktop : [1199, 4], //5 items between 1000px and 901px
				  itemsDesktopSmall : [768, 3], // betweem 900px and 601px
				  itemsTablet: [480, 2], //2 items between 600 and 0
				  itemsMobile : false, // itemsMobile disabled - inherit from itemsTablet option
					pagination : false,
					paginationNumbers: false,
				});
        
        // CAROUSEL CLIENTS AUTO PLAY 
			  $(".owl-clients-auto").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          autoPlay : 5000,
				  items : 5,
				  itemsDesktop : [1000,4], 
          itemsDesktopSmall : [900,3], 
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : false,
					paginationNumbers: false,
			 
			  });
		 
        // CAROUSEL CLIENTS NO AUTO PLAY  
			  $(".owl-clients-no-auto").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          //autoPlay : 5000,
				  items : 5,
				  itemsDesktop : [1000,4],
          itemsDesktopSmall : [900,3], 
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : true,
					paginationNumbers: false,
			 
			  });
		 
        // CAROUSEL 3 ITEMS NAV NO AUTO PLAY 
			  $(".owl-3items-nav").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          //autoPlay : 5000,
				  items : 4,
				  itemsDesktop : [1000,3], 
          itemsDesktopSmall : [900,2],
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : false,
					paginationNumbers: false,
					
					// Navigation
					navigation : true,
					navigationText : ["<span class='icon icon-arrows-left'></span>", "<i class='icon icon-arrows-right'></span>"],
					rewindNav : true,
					scrollPerPage : false,
			 
			  });

        // CAROUSEL CLIENTS NAV NO AUTO PLAY
			  $(".owl-clients-nav").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          //autoPlay : 5000,
				  items : 5,
				  itemsDesktop : [1000,4], 
          itemsDesktopSmall : [900,3],
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : false,
					paginationNumbers: false,
					
					// Navigation
					navigation : true,
					navigationText : ["<span class='icon icon-arrows-left'></span>", "<i class='icon icon-arrows-right'></span>"],
					rewindNav : true,
					scrollPerPage : false,
			 
			  });
		 
        // CAROUSEL ONE ITEM INLINE, NO CONTROLS, NO AUTO PLAY, WITH PAGINATION  
			  $(".owl-1-pag").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          //autoPlay : 5000,
				  items : 1,
				  itemsDesktop : [1000,1], 
					itemsDesktopSmall : [900,1], 
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : true,
					paginationNumbers: false,
			 
			  });

        // CAROUSEL ONE ITEM INLINE, NO CONTROLS, AUTO PLAY, WITH PAGINATION
			  $(".owl-1-pag-auto").owlCarousel({
			 
				  //Set AutoPlay to 3 seconds
          autoPlay : 5000,
				  items : 1,
				  itemsDesktop : [1000,1], 
					itemsDesktopSmall : [900,1], 
          itemsTablet: [470,1], 
          itemsMobile : false, 
				  
				  //Pagination
					pagination : true,
					paginationNumbers: false,
			 
			  });
 
        function center(number){
            var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
            var num = number;
            var found = false;
            for (var i in sync2visible) {
                if (num === sync2visible[i]) {
                    var found = true;
                }
            }
            if (found === false) {
                if (num > sync2visible[sync2visible.length - 1]) {
                    sync2.trigger("owl.goTo", num - sync2visible.length + 2)
                }
                else {
                    if (num - 1 === -1) {
                        num = 0;
                    }
                    sync2.trigger("owl.goTo", num);
                }
            }
            else 
                if (num === sync2visible[sync2visible.length - 1]) {
                    sync2.trigger("owl.goTo", sync2visible[1])
                }
                else 
                    if (num === sync2visible[0]) {
                        sync2.trigger("owl.goTo", num - 1)
                    }
        }
          
        var owl = $(".fullwidth-slideshow").data("owlCarousel");
        
        $(document.documentElement).keyup(function(event){
            // handle cursor keys
            if (event.keyCode == 37) {
                owl.prev();
            }
            else 
                if (event.keyCode == 39) {
                    owl.next();
                }
        });
        
        if ($(".owl-carousel").lenth) {
            var owl = $(".owl-carousel").data('owlCarousel');
            owl.reinit();
        }

    })(jQuery);
};

/* --------------------------------------------
  NEWSLETTER
--------------------------------------------- */
$(function () {
'use strict';
  var $form = $('#mc-embedded-subscribe-form');

  $('#mc-embedded-subscribe').on('click', function(event) {
	if(event) event.preventDefault();
	register($form);
  });
});

function register($form) {
  $.ajax({
	type: $form.attr('method'),
	url: $form.attr('action'),
	data: $form.serialize(),
	cache       : false,
	dataType    : 'json',
	contentType: "application/json; charset=utf-8",
	error       : function(err) { $('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>Could not connect to server. Please try again later.</div>'); },
	success     : function(data) {
	 
	  if (data.result != "success") {
		var message = data.msg;
		$('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+message+'</div>');
	  } 

	  else {
		var message = data.msg;
		$('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+message+'</div>');
	  }
	}
  });
}
//END NEWSLETTER	-------------------------------------------------------------------			


//WOW ANIMATE PLUGIN-------------------------------------------------------------------
/*! WOW - v1.1.2 - 2015-04-07
* Copyright (c) 2015 Matthieu Aussaguel; Licensed MIT */(function(){var a,b,c,d,e,f=function(a,b){return function(){return a.apply(b,arguments)}},g=[].indexOf||function(a){for(var b=0,c=this.length;c>b;b++)if(b in this&&this[b]===a)return b;return-1};b=function(){function a(){}return a.prototype.extend=function(a,b){var c,d;for(c in b)d=b[c],null==a[c]&&(a[c]=d);return a},a.prototype.isMobile=function(a){return/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(a)},a.prototype.createEvent=function(a,b,c,d){var e;return null==b&&(b=!1),null==c&&(c=!1),null==d&&(d=null),null!=document.createEvent?(e=document.createEvent("CustomEvent"),e.initCustomEvent(a,b,c,d)):null!=document.createEventObject?(e=document.createEventObject(),e.eventType=a):e.eventName=a,e},a.prototype.emitEvent=function(a,b){return null!=a.dispatchEvent?a.dispatchEvent(b):b in(null!=a)?a[b]():"on"+b in(null!=a)?a["on"+b]():void 0},a.prototype.addEvent=function(a,b,c){return null!=a.addEventListener?a.addEventListener(b,c,!1):null!=a.attachEvent?a.attachEvent("on"+b,c):a[b]=c},a.prototype.removeEvent=function(a,b,c){return null!=a.removeEventListener?a.removeEventListener(b,c,!1):null!=a.detachEvent?a.detachEvent("on"+b,c):delete a[b]},a.prototype.innerHeight=function(){return"innerHeight"in window?window.innerHeight:document.documentElement.clientHeight},a}(),c=this.WeakMap||this.MozWeakMap||(c=function(){function a(){this.keys=[],this.values=[]}return a.prototype.get=function(a){var b,c,d,e,f;for(f=this.keys,b=d=0,e=f.length;e>d;b=++d)if(c=f[b],c===a)return this.values[b]},a.prototype.set=function(a,b){var c,d,e,f,g;for(g=this.keys,c=e=0,f=g.length;f>e;c=++e)if(d=g[c],d===a)return void(this.values[c]=b);return this.keys.push(a),this.values.push(b)},a}()),a=this.MutationObserver||this.WebkitMutationObserver||this.MozMutationObserver||(a=function(){function a(){"undefined"!=typeof console&&null!==console&&console.warn("MutationObserver is not supported by your browser."),"undefined"!=typeof console&&null!==console&&console.warn("WOW.js cannot detect dom mutations, please call .sync() after loading new content.")}return a.notSupported=!0,a.prototype.observe=function(){},a}()),d=this.getComputedStyle||function(a){return this.getPropertyValue=function(b){var c;return"float"===b&&(b="styleFloat"),e.test(b)&&b.replace(e,function(a,b){return b.toUpperCase()}),(null!=(c=a.currentStyle)?c[b]:void 0)||null},this},e=/(\-([a-z]){1})/g,this.WOW=function(){function e(a){null==a&&(a={}),this.scrollCallback=f(this.scrollCallback,this),this.scrollHandler=f(this.scrollHandler,this),this.resetAnimation=f(this.resetAnimation,this),this.start=f(this.start,this),this.scrolled=!0,this.config=this.util().extend(a,this.defaults),this.animationNameCache=new c,this.wowEvent=this.util().createEvent(this.config.boxClass)}return e.prototype.defaults={boxClass:"wow",animateClass:"animated",offset:0,mobile:!0,live:!0,callback:null},e.prototype.init=function(){var a;return this.element=window.document.documentElement,"interactive"===(a=document.readyState)||"complete"===a?this.start():this.util().addEvent(document,"DOMContentLoaded",this.start),this.finished=[]},e.prototype.start=function(){var b,c,d,e;if(this.stopped=!1,this.boxes=function(){var a,c,d,e;for(d=this.element.querySelectorAll("."+this.config.boxClass),e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.all=function(){var a,c,d,e;for(d=this.boxes,e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.boxes.length)if(this.disabled())this.resetStyle();else for(e=this.boxes,c=0,d=e.length;d>c;c++)b=e[c],this.applyStyle(b,!0);return this.disabled()||(this.util().addEvent(window,"scroll",this.scrollHandler),this.util().addEvent(window,"resize",this.scrollHandler),this.interval=setInterval(this.scrollCallback,50)),this.config.live?new a(function(a){return function(b){var c,d,e,f,g;for(g=[],c=0,d=b.length;d>c;c++)f=b[c],g.push(function(){var a,b,c,d;for(c=f.addedNodes||[],d=[],a=0,b=c.length;b>a;a++)e=c[a],d.push(this.doSync(e));return d}.call(a));return g}}(this)).observe(document.body,{childList:!0,subtree:!0}):void 0},e.prototype.stop=function(){return this.stopped=!0,this.util().removeEvent(window,"scroll",this.scrollHandler),this.util().removeEvent(window,"resize",this.scrollHandler),null!=this.interval?clearInterval(this.interval):void 0},e.prototype.sync=function(){return a.notSupported?this.doSync(this.element):void 0},e.prototype.doSync=function(a){var b,c,d,e,f;if(null==a&&(a=this.element),1===a.nodeType){for(a=a.parentNode||a,e=a.querySelectorAll("."+this.config.boxClass),f=[],c=0,d=e.length;d>c;c++)b=e[c],g.call(this.all,b)<0?(this.boxes.push(b),this.all.push(b),this.stopped||this.disabled()?this.resetStyle():this.applyStyle(b,!0),f.push(this.scrolled=!0)):f.push(void 0);return f}},e.prototype.show=function(a){return this.applyStyle(a),a.className=a.className+" "+this.config.animateClass,null!=this.config.callback&&this.config.callback(a),this.util().emitEvent(a,this.wowEvent),this.util().addEvent(a,"animationend",this.resetAnimation),this.util().addEvent(a,"oanimationend",this.resetAnimation),this.util().addEvent(a,"webkitAnimationEnd",this.resetAnimation),this.util().addEvent(a,"MSAnimationEnd",this.resetAnimation),a},e.prototype.applyStyle=function(a,b){var c,d,e;return d=a.getAttribute("data-wow-duration"),c=a.getAttribute("data-wow-delay"),e=a.getAttribute("data-wow-iteration"),this.animate(function(f){return function(){return f.customStyle(a,b,d,c,e)}}(this))},e.prototype.animate=function(){return"requestAnimationFrame"in window?function(a){return window.requestAnimationFrame(a)}:function(a){return a()}}(),e.prototype.resetStyle=function(){var a,b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],e.push(a.style.visibility="visible");return e},e.prototype.resetAnimation=function(a){var b;return a.type.toLowerCase().indexOf("animationend")>=0?(b=a.target||a.srcElement,b.className=b.className.replace(this.config.animateClass,"").trim()):void 0},e.prototype.customStyle=function(a,b,c,d,e){return b&&this.cacheAnimationName(a),a.style.visibility=b?"hidden":"visible",c&&this.vendorSet(a.style,{animationDuration:c}),d&&this.vendorSet(a.style,{animationDelay:d}),e&&this.vendorSet(a.style,{animationIterationCount:e}),this.vendorSet(a.style,{animationName:b?"none":this.cachedAnimationName(a)}),a},e.prototype.vendors=["moz","webkit"],e.prototype.vendorSet=function(a,b){var c,d,e,f;d=[];for(c in b)e=b[c],a[""+c]=e,d.push(function(){var b,d,g,h;for(g=this.vendors,h=[],b=0,d=g.length;d>b;b++)f=g[b],h.push(a[""+f+c.charAt(0).toUpperCase()+c.substr(1)]=e);return h}.call(this));return d},e.prototype.vendorCSS=function(a,b){var c,e,f,g,h,i;for(h=d(a),g=h.getPropertyCSSValue(b),f=this.vendors,c=0,e=f.length;e>c;c++)i=f[c],g=g||h.getPropertyCSSValue("-"+i+"-"+b);return g},e.prototype.animationName=function(a){var b;try{b=this.vendorCSS(a,"animation-name").cssText}catch(c){b=d(a).getPropertyValue("animation-name")}return"none"===b?"":b},e.prototype.cacheAnimationName=function(a){return this.animationNameCache.set(a,this.animationName(a))},e.prototype.cachedAnimationName=function(a){return this.animationNameCache.get(a)},e.prototype.scrollHandler=function(){return this.scrolled=!0},e.prototype.scrollCallback=function(){var a;return!this.scrolled||(this.scrolled=!1,this.boxes=function(){var b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],a&&(this.isVisible(a)?this.show(a):e.push(a));return e}.call(this),this.boxes.length||this.config.live)?void 0:this.stop()},e.prototype.offsetTop=function(a){for(var b;void 0===a.offsetTop;)a=a.parentNode;for(b=a.offsetTop;a=a.offsetParent;)b+=a.offsetTop;return b},e.prototype.isVisible=function(a){var b,c,d,e,f;return c=a.getAttribute("data-wow-offset")||this.config.offset,f=window.pageYOffset,e=f+Math.min(this.element.clientHeight,this.util().innerHeight())-c,d=this.offsetTop(a),b=d+a.clientHeight,e>=d&&b>=f},e.prototype.util=function(){return null!=this._util?this._util:this._util=new b},e.prototype.disabled=function(){return!this.config.mobile&&this.util().isMobile(navigator.userAgent)},e}()}).call(this);

//EQUAL HEIGHTS PLUGIN-------------------------------------------------------------------
   /*!
   * Simple jQuery Equal Heights
   *
   * Copyright (c) 2013 Matt Banks
   * Dual licensed under the MIT and GPL licenses.
   * Uses the same license as jQuery, see:
   * http://docs.jquery.com/License
   *
   * @version 1.6.0
   */
  /* !function(a){a.fn.equalHeights=function(){var b=0,c=a(this);return c.each(function(){var c=a(this).innerHeight();c>b&&(b=c)}),c.css("height",b)},a("[data-equal]").each(function(){var b=a(this),c=b.data("equal");b.find(c).equalHeights()})}(jQuery); */
  
//SMOOTHSCROLL PLUGIN-------------------------------------------------------------------  
/*if (navigator.appVersion.indexOf("Win")!=-1) {

	// SmoothScroll for websites v1.4.9
	// Licensed under the terms of the MIT license.

	// People involved
	//  - Balazs Galambosi (maintainer)  
	//  - Michael Herf     (Pulse Algorithm)
!function(){var s,i,c,a,o={frameRate:150,animationTime:500,stepSize:150,pulseAlgorithm:!0,pulseScale:6,pulseNormalize:1,accelerationDelta:20,accelerationMax:1,keyboardSupport:!0,arrowScroll:50,fixedBackground:!0,excluded:""},p=o,u=!1,d=!1,l={x:0,y:0},f=!1,m=document.documentElement,h=[],w=/^Mac/.test(navigator.platform),v={left:37,up:38,right:39,down:40,spacebar:32,pageup:33,pagedown:34,end:35,home:36},y={37:1,38:1,39:1,40:1};function b(){if(!f&&document.body){f=!0;var e=document.body,t=document.documentElement,o=window.innerHeight,n=e.scrollHeight;if(m=0<=document.compatMode.indexOf("CSS")?t:e,s=e,p.keyboardSupport&&Y("keydown",D),top!=self)d=!0;else if(Q&&o<n&&(e.offsetHeight<=o||t.offsetHeight<=o)){var r,a=document.createElement("div");a.style.cssText="position:absolute; z-index:-10000; top:0; left:0; right:0; height:"+m.scrollHeight+"px",document.body.appendChild(a),c=function(){r||(r=setTimeout(function(){u||(a.style.height="0",a.style.height=m.scrollHeight+"px",r=null)},500))},setTimeout(c,10),Y("resize",c);if((i=new R(c)).observe(e,{attributes:!0,childList:!0,characterData:!1}),m.offsetHeight<=o){var l=document.createElement("div");l.style.clear="both",e.appendChild(l)}}p.fixedBackground||u||(e.style.backgroundAttachment="scroll",t.style.backgroundAttachment="scroll")}}var g=[],S=!1,x=Date.now();function k(d,f,m){var e,t;if(e=0<(e=f)?1:-1,t=0<(t=m)?1:-1,(l.x!==e||l.y!==t)&&(l.x=e,l.y=t,g=[],x=0),1!=p.accelerationMax){var o=Date.now()-x;if(o<p.accelerationDelta){var n=(1+50/o)/2;1<n&&(n=Math.min(n,p.accelerationMax),f*=n,m*=n)}x=Date.now()}if(g.push({x:f,y:m,lastX:f<0?.99:-.99,lastY:m<0?.99:-.99,start:Date.now()}),!S){var r=q(),h=d===r||d===document.body;null==d.$scrollBehavior&&function(e){var t=M(e);if(null==B[t]){var o=getComputedStyle(e,"")["scroll-behavior"];B[t]="smooth"==o}return B[t]}(d)&&(d.$scrollBehavior=d.style.scrollBehavior,d.style.scrollBehavior="auto");var w=function(e){for(var t=Date.now(),o=0,n=0,r=0;r<g.length;r++){var a=g[r],l=t-a.start,i=l>=p.animationTime,c=i?1:l/p.animationTime;p.pulseAlgorithm&&(c=F(c));var s=a.x*c-a.lastX>>0,u=a.y*c-a.lastY>>0;o+=s,n+=u,a.lastX+=s,a.lastY+=u,i&&(g.splice(r,1),r--)}h?window.scrollBy(o,n):(o&&(d.scrollLeft+=o),n&&(d.scrollTop+=n)),f||m||(g=[]),g.length?j(w,d,1e3/p.frameRate+1):(S=!1,null!=d.$scrollBehavior&&(d.style.scrollBehavior=d.$scrollBehavior,d.$scrollBehavior=null))};j(w,d,0),S=!0}}function e(e){f||b();var t=e.target;if(e.defaultPrevented||e.ctrlKey)return!0;if(N(s,"embed")||N(t,"embed")&&/\.pdf/i.test(t.src)||N(s,"object")||t.shadowRoot)return!0;var o=-e.wheelDeltaX||e.deltaX||0,n=-e.wheelDeltaY||e.deltaY||0;w&&(e.wheelDeltaX&&K(e.wheelDeltaX,120)&&(o=e.wheelDeltaX/Math.abs(e.wheelDeltaX)*-120),e.wheelDeltaY&&K(e.wheelDeltaY,120)&&(n=e.wheelDeltaY/Math.abs(e.wheelDeltaY)*-120)),o||n||(n=-e.wheelDelta||0),1===e.deltaMode&&(o*=40,n*=40);var r=z(t);return r?!!function(e){if(!e)return;h.length||(h=[e,e,e]);e=Math.abs(e),h.push(e),h.shift(),clearTimeout(a),a=setTimeout(function(){try{localStorage.SS_deltaBuffer=h.join(",")}catch(e){}},1e3);var t=120<e&&P(e);return!P(120)&&!P(100)&&!t}(n)||(1.2<Math.abs(o)&&(o*=p.stepSize/120),1.2<Math.abs(n)&&(n*=p.stepSize/120),k(r,o,n),e.preventDefault(),void C()):!d||!W||(Object.defineProperty(e,"target",{value:window.frameElement}),parent.wheel(e))}function D(e){var t=e.target,o=e.ctrlKey||e.altKey||e.metaKey||e.shiftKey&&e.keyCode!==v.spacebar;document.body.contains(s)||(s=document.activeElement);var n=/^(button|submit|radio|checkbox|file|color|image)$/i;if(e.defaultPrevented||/^(textarea|select|embed|object)$/i.test(t.nodeName)||N(t,"input")&&!n.test(t.type)||N(s,"video")||function(e){var t=e.target,o=!1;if(-1!=document.URL.indexOf("www.youtube.com/watch"))do{if(o=t.classList&&t.classList.contains("html5-video-controls"))break}while(t=t.parentNode);return o}(e)||t.isContentEditable||o)return!0;if((N(t,"button")||N(t,"input")&&n.test(t.type))&&e.keyCode===v.spacebar)return!0;if(N(t,"input")&&"radio"==t.type&&y[e.keyCode])return!0;var r=0,a=0,l=z(s);if(!l)return!d||!W||parent.keydown(e);var i=l.clientHeight;switch(l==document.body&&(i=window.innerHeight),e.keyCode){case v.up:a=-p.arrowScroll;break;case v.down:a=p.arrowScroll;break;case v.spacebar:a=-(e.shiftKey?1:-1)*i*.9;break;case v.pageup:a=.9*-i;break;case v.pagedown:a=.9*i;break;case v.home:l==document.body&&document.scrollingElement&&(l=document.scrollingElement),a=-l.scrollTop;break;case v.end:var c=l.scrollHeight-l.scrollTop-i;a=0<c?c+10:0;break;case v.left:r=-p.arrowScroll;break;case v.right:r=p.arrowScroll;break;default:return!0}k(l,r,a),e.preventDefault(),C()}function t(e){s=e.target}var n,r,M=(n=0,function(e){return e.uniqueID||(e.uniqueID=n++)}),E={},T={},B={};function C(){clearTimeout(r),r=setInterval(function(){E=T=B={}},1e3)}function H(e,t,o){for(var n=o?E:T,r=e.length;r--;)n[M(e[r])]=t;return t}function z(e){var t=[],o=document.body,n=m.scrollHeight;do{var r=(!1?E:T)[M(e)];if(r)return H(t,r);if(t.push(e),n===e.scrollHeight){var a=O(m)&&O(o)||X(m);if(d&&L(m)||!d&&a)return H(t,q())}else if(L(e)&&X(e))return H(t,e)}while(e=e.parentElement)}function L(e){return e.clientHeight+10<e.scrollHeight}function O(e){return"hidden"!==getComputedStyle(e,"").getPropertyValue("overflow-y")}function X(e){var t=getComputedStyle(e,"").getPropertyValue("overflow-y");return"scroll"===t||"auto"===t}function Y(e,t,o){window.addEventListener(e,t,o||!1)}function A(e,t,o){window.removeEventListener(e,t,o||!1)}function N(e,t){return e&&(e.nodeName||"").toLowerCase()===t.toLowerCase()}if(window.localStorage&&localStorage.SS_deltaBuffer)try{h=localStorage.SS_deltaBuffer.split(",")}catch(e){}function K(e,t){return Math.floor(e/t)==e/t}function P(e){return K(h[0],e)&&K(h[1],e)&&K(h[2],e)}var $,j=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||function(e,t,o){window.setTimeout(e,o||1e3/60)},R=window.MutationObserver||window.WebKitMutationObserver||window.MozMutationObserver,q=($=document.scrollingElement,function(){if(!$){var e=document.createElement("div");e.style.cssText="height:10000px;width:1px;",document.body.appendChild(e);var t=document.body.scrollTop;document.documentElement.scrollTop,window.scrollBy(0,3),$=document.body.scrollTop!=t?document.body:document.documentElement,window.scrollBy(0,-3),document.body.removeChild(e)}return $});function V(e){var t;return((e*=p.pulseScale)<1?e-(1-Math.exp(-e)):(e-=1,(t=Math.exp(-1))+(1-Math.exp(-e))*(1-t)))*p.pulseNormalize}function F(e){return 1<=e?1:e<=0?0:(1==p.pulseNormalize&&(p.pulseNormalize/=V(1)),V(e))}var I=window.navigator.userAgent,_=/Edge/.test(I),W=/chrome/i.test(I)&&!_,U=/safari/i.test(I)&&!_,G=/mobile/i.test(I),J=/Windows NT 6.1/i.test(I)&&/rv:11/i.test(I),Q=U&&(/Version\/8/i.test(I)||/Version\/9/i.test(I)),Z=(W||U||J)&&!G,ee=!1;try{window.addEventListener("test",null,Object.defineProperty({},"passive",{get:function(){ee=!0}}))}catch(e){}var te=!!ee&&{passive:!1},oe="onwheel"in document.createElement("div")?"wheel":"mousewheel";function ne(e){for(var t in e)o.hasOwnProperty(t)&&(p[t]=e[t])}oe&&Z&&(Y(oe,e,te),Y("mousedown",t),Y("load",b)),ne.destroy=function(){i&&i.disconnect(),A(oe,e),A("mousedown",t),A("keydown",D),A("resize",c),A("load",b)},window.SmoothScrollOptions&&ne(window.SmoothScrollOptions),"function"==typeof define&&define.amd?define(function(){return ne}):"object"==typeof exports?module.exports=ne:window.SmoothScroll=ne}();

};*/
//SMOOTHSCROLL END-------------------------------------------------

//NAV STICK 2 MENU-------------------------------------------------------------------
function initNavStick2(){
 
  $(window).scroll(function(){        
 
    if ($(window).scrollTop() > 10) {
      $("#nav-stick2").removeClass("transparent").addClass("has-bg");
    }
    else {
      $("#nav-stick2").addClass("transparent").removeClass("has-bg");
    }
  
  });
};
