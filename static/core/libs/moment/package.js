var profile = {
    resourceTags: {
        ignore: function(filename, mid){
            // only admin moment/moment
            return mid != "moment/moment";
        },
        amd: function(filename, mid){
            return /\.js$/.test(filename);
        }
    }
};
