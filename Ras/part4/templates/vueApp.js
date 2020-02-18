Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";

new Vue({
    el: '#part4_1',
    delimiters: ['${','}'],
    data() {
        return {
            info: null,
            lines: [
                {text: 'Р-409, З-419П1, З-419МП', value: '6'},
                {text: 'З-416ГМ', value: '3'},
                {text: 'Р-431АМ', value: '4'},
                {text: 'Р-423АМ', value: '4'},

            ],
            line_selected: '',
            canals: [
                {text: 'ТГ', value: '2'},
                {text: 'ТЧ', value: '2'},
                {text: 'Цифровой поток (канал)', value: '1.4'},
                {selected: ''},
            ],
            canal_selected: '',
            number_val: '',
            loading: true,
            currentArticle: {},

            newArticle: {'line_sel': null, 'canal_sel': null, 'number': null},
            search_term: '',
        };
    },
    mounted() {
        axios
            .get('https://api.coindesk.com/v1/bpi/currentprice.json')
            .then(response => (this.info = response));
    }




});