Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#part4_1',
    delimiters: ['${','}'],
    data: {

        lines: [
            { text: 'Р-409, З-419П1, З-419МП', value: '6' },
            { text: 'З-416ГМ', value: '3' },
            { text: 'Р-431АМ', value: '4' },
            { text: 'Р-423АМ', value: '4' },

        ],
        line_selected: '',
        canals: [
            { text: 'ТГ', value: '2' },
            { text: 'ТЧ', value: '2' },
            { text: 'Цифровой поток (канал)', value: '1.4' },
            {selected: ''},
        ],
        canal_selected: '',

        number_val: '',

        loading: true,
        currentArticle: {},
        message: null,
        newArticle: { 'part4_id': null, 'line_selected': null, 'canal_selected': null, 'number_val': null },
        search_term: '',
    },
    mounted: function() {
        this.getLines();
    },
    methods: {
        getArticles: function() {
            let api_url = '/api/part4/';
            if(this.search_term!==''||this.search_term!==null) {
                api_url = `/api/part4/?search=${this.search_term}`
            }
            this.loading = true;
            this.$http.get(api_url)
                .then((response) => {
                    this.articles = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getArticle: function(id) {
            this.loading = true;
            this.$http.get(`/api/part4/${id}/`)
                .then((response) => {
                    this.currentArticle = response.data;
                    $("#editArticleModal").modal('show');
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addArticle: function() {
            this.loading = true;
            this.$http.post('/api/part4/',this.newArticle)
                .then((response) => {
                    this.loading = true;
                    this.getArticles();
                })
                .catch((err) => {
                    this.loading = true;
                    console.log(err);
                })
        },
        // updateArticle: function() {
        //   this.loading = true;
        //   this.$http.put(`/api/part4/${this.currentArticle.part4_id}/`, this.currentArticle)
        //           .then((response) => {
        //             this.loading = false;
        //             this.currentArticle = response.data;
        //             this.getArticles();
        //           })
        //           .catch((err) => {
        //             this.loading = false;
        //             console.log(err);
        //           })
        // },
        updateFirst: function() {
            this.loading = true;
            this.$http.put(`/api/part4/data/`, this.currentArticle)
                .then((response) => {
                    this.loading = false;
                    this.currentArticle = response.data;
                    this.getArticles();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        deleteArticle: function(id) {
            this.loading = true;
            this.$http.delete(`/api/part4/${id}/`)
                .then((response) => {
                    this.loading = false;
                    this.getArticles();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        }
    }
});