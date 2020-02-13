<template>
    <div>
        <ul>

            <item
            v-for="each in massiv"
            v-bind:each="each"
            />

        </ul>
    </div>

</template>
<script>
import item from '@/components/item'
export default{
    props:['massiv'],
    components:{
        item
        }

    }
</script>
