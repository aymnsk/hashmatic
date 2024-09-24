$(document).ready(function() {
    $('#uploadForm').on('submit', function(e) {
        e.preventDefault();
        
        let formData = new FormData();
        let file = $('#file')[0].files[0];
        
        if (file) {
            formData.append('file', file);
        }

        $.ajax({
            type: 'POST',
            url: '/api/upload',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#message').html(`<div class="alert alert-success">${response.message}</div>`);
                if (response.file_path) {
                    $('#message').append(`<p>Uploaded file: <a href="${response.file_path}" target="_blank">${response.file_path}</a></p>`);
                }
                $('#file').val(''); // Clear the file input
            },
            error: function() {
                $('#message').html('<div class="alert alert-danger">Error uploading file!</div>');
            }
        });
    });
});
