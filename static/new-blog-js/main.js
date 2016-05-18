

$(document).ready(function(){


    $('.login-btn').click(function(){
      $('.login-wrapper').show();
      $('body').css('overflow', 'hidden');
    });
    $('.login-close').click(function(){
      $('.login-wrapper').hide();
      $('body').css("overflow", "none");
    });
     $('.sign-up-btn').click(function(){
      $('.sign-up-wrapper').show();
      $('body').css("overflow", "hidden");
    });
     $('.sign-up-close').click(function(){
      $('.sign-up-wrapper').hide();
      $('body').css("overflow", "none");
    });

  
  $(".faq_Q").click(function(){
    if(!$(this).is('.active')){
      $('.faq_Q').removeClass('active');
      $(this).addClass('active');
    }else{
      $(this).find('.minus-icon').css('display','none');
      $(this).find('.plus-icon').css('display','inline-block');
      $(this).removeClass('active');
      $(this).next('.faq_A').slideUp(350);
      return;
    }
    $('.faq_Q').find('.minus-icon').css('display','none');
    $('.faq_Q').find('.plus-icon').css('display','inline-block');
    $(this).find('.plus-icon').css('display','none');
    $(this).find('.minus-icon').css('display','inline-block');
    $(".faq_A").slideUp(350);
    $(this).next().slideDown(350);
  });
    
    
  var show_class;
  $(".faq_Q_A").hide();
    $(".horizontalRule").hide();
    $(".faq").show();
  $(".careers").hide();
    $(".aboutus").hide();
    $(".contactus").hide();
  $(".ideation").show();
    $(".privacy").show();
    $(".frontenddeveloper").show();
  $(".page_right_link").click(function(){
    $(".page_right_link").removeClass('page_right_link_highlight');
    $(this).addClass('page_right_link_highlight');
    //$(".faq_Q_A").hide();
    //$(".ideation").show();
      //$(".privacy").show();
      $(".frontenddeveloper").show();
    $(".page_Q_A").hide();
        $(".horizontalRule").hide();
    show_class = $(this).text().toLowerCase().replace(/ /g, '');
        //show_class = $.trim(show_class);
        // show_class = $.replace(/ /g,'');
        //alert(show_class);
    $("."+show_class).fadeIn(200);
  });
  $(".faq_right_link").click(function(){
    $(".faq_right_link").removeClass('faq_right_link_highlight');
    $(this).addClass('faq_right_link_highlight');
    $(".faq_Q_A").hide();
    //$(".page_Q_A").hide();
        $(".horizontalRule").hide();
    show_class = $(this).text().toLowerCase().replace(/ /g, '');
        //show_class = $.trim(show_class);
        // show_class = $.replace(/ /g,'');
        //alert(show_class);
    $("."+show_class).fadeIn(200);
  });

  
  /*$(".page_right_link").click(function(){
    $(".page_right_link").removeClass('page_right_link_highlight');
    $(this).addClass('page_right_link_highlight');
    //$(".faq_Q_A").hide();
        $(".ideation").show();
        $(".privacy").show();
        $(".frontenddeveloper").show();
        $(".horizontalRule").hide();
    show_class = $(this).text().toLowerCase().replace(/ /g, '');
        //show_class = $.trim(show_class);
        // show_class = $.replace(/ /g,'');
        //alert(show_class);
    $("."+show_class).fadeIn(200);
  });*/

  var hash = window.location.hash;
  console.log($(hash+'-link'));
  if(hash)
    $(hash+'-link').trigger('click');
    });

$(document).ready(function(){

    $('.menu-anchor').on('click touchstart', function(e){
    $('html').toggleClass('menu-active');
      e.preventDefault();
    });


    $(".sectionals").click(function(){
      $(this).parent().find(".desc").css("height","100%");
      $(this).parent().find(".comment-section").css("display","block");
    });


    $(function () {
    $('.navbar-toggle-sidebar').click(function () {
      $('.navbar-nav').toggleClass('slide-in');
      $('.side-body').toggleClass('body-slide-in');
      $('#search').removeClass('in').addClass('collapse').slideUp(200);
    });


    $('#search-trigger').click(function () {
      $('.navbar-nav').removeClass('slide-in');
      $('.side-body').removeClass('body-slide-in');
      $('.search-input').focus();
    });


    $('.navbar-nav li').click(function(){
      $(this).addClass('active');
    });
  });
    

   $(function(){
        $('#my-form-builder').formbuilder({
          'save_url': 'example-save.php',
          'load_url': 'example-json.php',
          'useJson' : true
        });
        $(function() {
          $("#my-form-builder ul").sortable({ opacity: 0.6, cursor: 'move'});
        });
      });


  $('.new-topic').click(function(){ 
    
    $("select.input-sm").css("display", "block");
    $(".captcha").css("display", "block");
    $(".submit-row button").css("display", "block");
    $(".mce-panel").removeClass("important");
       
  });

  
  $('.close-btn').click(function(){  
    $("select.input-sm").css("display", "none");
    $(".captcha").css("display", "none");
    $(".submit-row button").css("display", "none");
    $(".mce-panel").addClass("important");
  });


 $('.blog-search').click(function(){ 
    $(".search-blog-results").toggle();    
  });


 $('.idea-box').click(function(){ 
    
    $(this).toggleClass("selected");
       
  });

 //$('.html5fileupload.demo_multi').html5fileupload();


  $('.comment').click(function(){
    $(this).animate({height:'200px'}, 500);
  });


  $(".btn-top").click(function() {
    $("html, body").animate({
      scrollTop: $($(this).attr("href")).offset().top 
    }, 1000);
    return false;
  });


  $('.dz-error-mark').click(function(){
      $(this).find('.dz-image').remove();
  });


  $('.show-more').click(function(){
    $('.problem-mention').css("height", "+=50");
  });


	$('.research').click(function() {
	 $('.collaborate-output').hide();
	 $('.research-output').show();
	 $(this).css("border-bottom", "4px solid #009aae");
	 $('.collaborate').css("border-bottom", "0px solid #009aae");
	});


	$('.collaborate').click(function() {
	 $('.collaborate-output').show();
	 $('.research-output').hide();
	  $(this).css("border-bottom", "4px solid #009aae");
	  $('.research').css("border-bottom", "0px solid #009aae");
	});

	
	$('#uploadImage').change(function(){
	     var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById("uploadPreview").src = oFREvent.target.result;
        };
   });


    $("#update_details").click(function(){
        $(".constant").hide();
        $(".edit").show();
        $("#edit_details_button").show();
        $("#exit_details_button").show();
        var $gender="female";
        if ($gender =="male")
          document.getElementById("optionsRadiosMale").checked=true;
        else
          document.getElementById("optionsRadiosFemale").checked=true;
    });

	 $("#update_biography").click(function(){
        $(".constant_biography").hide();
        $(".edit_biography").show();
        $("#inputBiography").show();
		    $("#edit_biography_button").show();
        $("#exit_biography_button").show();
      });
	
      $('#exit_details_button').click(function(){
          $(".constant").show();
          $(".edit").hide();
          $("#edit_details_button").hide();
          $("#exit_details_button").hide();
      });


	   $('#exit_biography_button').click(function(){
			$(".constant_biography").show();
			$(".edit_biography").hide();
			$("#edit_biography_button").hide();
			$("#exit_biography_button").hide();
      });


	  $('#exit_biography_button').click(function(){
			$(".constant_biography").show();
			$(".edit_biography").hide();
			$("#edit_biography_button").hide();
			$("#exit_biography_button").hide();
      });


     $(".sectionals .likes .fa-heart").click(function(){
        $(this).css("color", "#009aae");
     });




      tinymce.init({
      selector: "#texteditor",
      theme: "modern",
      plugins: [
          "advlist autolink lists link image charmap print preview hr anchor pagebreak",
          "searchreplace wordcount visualblocks visualchars code fullscreen",
          "insertdatetime media nonbreaking save table contextmenu directionality",
          "emoticons template paste textcolor colorpicker textpattern imagetools"
      ],
      toolbar1: "bold italic | alignleft aligncenter alignright alignjustify | link image | forecolor backcolor emoticons",
      toolbar2: "",
      image_advtab: true,
      templates: [
          {title: 'Test template 1', content: 'Test 1'},
          {title: 'Test template 2', content: 'Test 2'}
      ],
      file_browser_callback : 'myFileBrowser'
    });

    window.onload = function what(){
      document.getElementById('tinymce-28-0').innerHTML='';
    };

});


$(window).load(function(){
  //$('.pre-loader').hide();
  $(".mce-panel").addClass("important");

});

$(document).ready(function(){
  $(function(){

      $('#tags input').on('focusout',function(){    
        var txt= this.value.replace(/[^a-zA-Z0-9\+\-\.\#]/g,''); // allowed characters
        if(txt) {
          $('.selectedtags').append('<span class="tag">'+' '+txt.toLowerCase()+'<span class="glyphicon glyphicon-remove"></span>'+'</span>');
        }
        this.value="";
      }).on('keyup',function( e ){
        // if: comma,enter (delimit more keyCodes with | pipe)
        if(/(188|13)/.test(e.which)) $(this).focusout(); 

      });
      
      
      $('#tags').on('click','.tag',function(){
         // if(confirm("Really delete this tag?")) 
         $(this).remove(); 
      });

    });
    $(function(){

      $('#links input').on('focusout',function(){    
        var txt= this.value.replace(/[^a-zA-Z0-9\+\-\.\#]/g,''); // allowed characters
        if(txt) {
                onYouTubeIframeAPIReady(txt);
            // http://img.youtube.com/vi/lzXktIlm5zQ/mqdefault.jpg
            // https://www.youtube.com/watch?v=_2siOYD2P-8
          $('.selectedlinks').append('<span class="links">'+"<img src='http://img.youtube.com/vi/lzXktIlm5zQ/mqdefault.jpg'"+txt.toLowerCase()+'<span class="glyphicon glyphicon-remove"></span>'+'</span>');
        }
        this.value="";
      }).on('keyup',function( e ){
        // if: comma,enter (delimit more keyCodes with | pipe)
        if(/(188|13)/.test(e.which)) $(this).focusout(); 

      });
      
      
      $('#links').on('click','.links',function(){
         // if(confirm("Really delete this tag?")) 
         $(this).remove(); 
      });

    });
});

$(document).ready(function(){
    $(window, document, undefined).ready(function() {

      $('input').blur(function() {
        var $this = $(this);
        if ($this.val())
          $this.addClass('used');
        else
          $this.removeClass('used');
      });

      var $ripples = $('.ripples');

      $ripples.on('click.Ripples', function(e) {

        var $this = $(this);
        var $offset = $this.parent().offset();
        var $circle = $this.find('.ripplesCircle');

        var x = e.pageX - $offset.left;
        var y = e.pageY - $offset.top;

        $circle.css({
          top: y + 'px',
          left: x + 'px'
        });

        $this.addClass('is-active');

      });

      $ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function(e) {
        $(this).removeClass('is-active');
      });

    });
  });



