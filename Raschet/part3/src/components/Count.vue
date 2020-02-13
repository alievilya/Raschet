<template>
    <div class="pt-5">
        <form @submit.prevent="count" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="subscription.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter name"
                    :class="{'is-invalid': errors.has('subscription.name') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            subscription: {
                name: '',
                currency: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.currency)
                axios
                    .post('http://127.0.0.1:8000/api/test_count/',
                        this.subscription
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>