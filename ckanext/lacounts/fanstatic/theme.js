$(document).ready(function(){function closeSearch(){$(".page").addClass("inactive-search"),$(".page").removeClass("active-search"),$(".masthead .site-search .close").remove()}function openSearch(){$(".page").addClass("active-search"),$(".page").removeClass("inactive-search"),$(".site-search").append('<button class="close" type="button"><i class="fa fa-times" aria-hidden="true"></i><span class="sr-only">Close</span></button>');var firstInput=$(".active-search #field-sitewide-search"),lastInput=$(".active-search .masthead .site-search .close");lastInput.on("keydown",function(e){9!==e.which||e.shiftKey||(e.preventDefault(),firstInput.focus())}),firstInput.on("keydown",function(e){9===e.which&&e.shiftKey&&(e.preventDefault(),lastInput.focus())}),$(".active-search .masthead .site-search .close").on("click",function(){closeSearch()}),$(".active-search .masthead .site-search .close").on("keypress",function(e){13==e.which&&closeSearch()})}$(".page").addClass("inactive-search"),$(".masthead .site-search label").attr("tabindex","0"),$(".inactive-search .masthead .site-search label").on("click",function(){openSearch()}),$(".inactive-search .masthead .site-search label").on("keypress",function(e){13==e.which&&(openSearch(),$("#field-sitewide-search").focus())}),$(".masthead").affix()});