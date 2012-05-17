$(function() {
    var swfuploadLoaded = function () {
        $('.button').html('上传文件<small style="font-weight:normal">(10M)</small>');
    };

    var fileDialogComplete = function (numFilesSelected, numFilesQueued) {
        try {
            this.startUpload();
        } catch (ex)  {
            alert(ex);
        }
    };

    var uploadStart = function (file) {
        console.log('begin upload');
    };

    var uploadSuccess = function (file, serverData) {
        console.log('Success');
        console.log(file.name);
        console.log(serverData);
        $('.upload-progress').append($('<li><a href="/img/'+serverData+'">'+file.name+'</a></li>'));
    };

    var uploadComplete = function (file) {
        //console.dir(file);
        console.log('complete');
        console.log(file.name);
    };

    var uploadError = function (file, errorCode, message) {
        console.log('Error');
        console.log(file.id);
        console.log(errorCode);
        console.log(message);
    };

    var uploadProgress = function (file, bytesLoaded, bytesTotal) {
        console.log('Progress');
    };

    var settings = {
        flash_url : "/static/swfupload/swfupload.swf",
        upload_url: "/upload_c",
        post_params: {},
        file_size_limit : "10 MB",
        file_types : "*.gif;*.jpg;*.png;*.tiff;*.bmp;",
        file_types_description : "图片文件",
        file_upload_limit : 0,
        file_queue_limit : 0,
        debug: false,

        //Handle Settings
        file_dialog_complete_handler : fileDialogComplete,
        upload_start_handler : uploadStart,
        upload_progress_handler : uploadProgress,
        upload_success_handler : uploadSuccess,
        queue_complete_handler : uploadComplete,
        upload_error_handler : uploadError,
        swfupload_loaded_handler : swfuploadLoaded,

        // Button Settings
        button_placeholder_id : "swfu-placeholder",
        button_height: 25,
        button_text: '上传',
        button_text_style: '',
        button_text_left_padding: 14,
        button_text_top_padding: 0,
        button_width: '150px',
        button_window_mode: SWFUpload.WINDOW_MODE.TRANSPARENT,
        button_cursor: SWFUpload.CURSOR.HAND
    };
    var swfu = new SWFUpload(settings);
});
