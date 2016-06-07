tinyMCE.init({
  	language : "en", 
        // General options
        mode : "textareas",
        theme : "advanced",
  	//theme : "simple",
        plugins : "syntaxhl,advimage,lists,pagebreak,style,table,save,advhr,advlink,emotions,inlinepopups,insertdatetime,media,searchreplace,contextmenu,paste,directionality,fullpage,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,tabfocus",
  	//plugins : "advhr,advimage,advlink,advlist,bbcode,contextmenu,directionality,emotions,fullpage,fullscreen,inlinepopups,insertdatetime,legactoutput,lists,media,nonbreaking,noneditable,pagebreak,paste,save,searchreplace,style,tabfocus,table,template,visualblocks,visualchars,xhtmlxtras",
        //plugins : "advimage,media",
        //plugins : "advimage,visualchars,nonbreaking,xhtmlxtras,template,tabfocus",
        // Theme options
        theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,code,syntaxhl",
        theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
        theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
        theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom",
        theme_advanced_resizing : true,
        remove_linebreaks : false, 
	extended_valid_elements : "textarea[cols|rows|disabled|name|readonly|class]",

        // Skin options
        skin : "o2k7",
  	//skin : "default",
        skin_variant : "silver",

        // Example content CSS (should be your site CSS)
        content_css : "css/example.css",

        // Drop lists for link/image/media/template dialogs
        template_external_list_url : "js/template_list.js",
        external_link_list_url : "js/link_list.js",
        external_image_list_url : "js/image_list.js",
        media_external_list_url : "js/media_list.js",

        // Replace values for the template plugin
        template_replace_values : {
                username : "Some User",
                staffid : "991234"
        }
});