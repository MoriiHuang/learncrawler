const projectPath='http://10.166.224.160:5000/register'
    const app = new Vue({
    el:"#app",
	data:{
	isShow:1,
	isRegister:0,
	},
	methods:{
	change(){
	this.isShow=0;
	},
	register(){
    this.isRegister=1;
    window.location.href=projectPath;
	}
	}
    })