(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-accountInfo-accountInfo"],{"39b9":function(n,t,o){"use strict";o.r(t);var i=function(){var n=this,t=n.$createElement,o=n._self._c||t;return o("v-uni-view",[o("v-uni-button",{attrs:{type:"primary"},on:{click:function(t){t=n.$handleEvent(t),n.getAccountInfo()}}},[n._v("获取账户信息")])],1)},e=[],c={data:function(){return{}},methods:{getAccountInfo:function(){console.log("come on");var n="eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiJjODQ3YzJjNi01ZDI0LTQ3MDMtODU5Mi02N2M2OWQ0ZGMyNDkiLCJleHAiOjE1NzgwNDA2NjUsImlhdCI6MTU0NjUwNDY2NSwiaXNzIjoiZmJkMjZiYzYtM2QwNC00OTY0LWE3ZmUtYTU0MDQzMmIxNmUyIn0.hJo0lZh4nlI-izuNKOJalbFM98c8Yh3jljrDmYsUXbqbbcJh9C-K9J4SAo-O7MrmOre312IRzpbm0g45rVThzO1bS4zc0GmDBZOicG6C_Lf30-MMFSPvJJh1U1tDipzcRGNYWMpgdrCF55K31bgYamSQ6XpnT8XH4EoWLcbX3Lo";uni.request({url:"https://api.mixin.one/assets",header:{Authorization:"Bearer "+n},method:"GET",success:function(n){var t=n.data;console.log(t)},fail:function(n){uni.showModal({title:"提示",content:"fail =="+JSON.stringify(n.data),showCancel:!1,confirmText:"确定"})}})}}},a=c,s=(o("5d1d"),o("2877")),u=Object(s["a"])(a,i,e,!1,null,"0fb537a2",null);u.options.__file="accountInfo.vue";t["default"]=u.exports},"5d1d":function(n,t,o){"use strict";var i=o("c955"),e=o.n(i);e.a},c955:function(n,t,o){var i=o("f2a9");"string"===typeof i&&(i=[[n.i,i,""]]),i.locals&&(n.exports=i.locals);var e=o("4f06").default;e("3be8a5d1",i,!0,{sourceMap:!1,shadowMode:!1})},f2a9:function(n,t,o){t=n.exports=o("2350")(!1),t.push([n.i,"",""])}}]);