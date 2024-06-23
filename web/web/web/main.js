import axios from "axios";

let params = new URLSearchParams(window.location.search);
let id = params.get("id");

import {setupViewer} from "./viewer/view"

axios.get("http://8.137.125.44:8940/get-pos" , {
    // url参数
    params:{
        id:id,
    }
}).then((value) =>{
    console.log(value.data)
    setupViewer('http://8.137.125.44:8940/model/' + value.data[0].position);
})