// components/role-box/role-box.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    role:{
      type:String
    },
    booker:{
      type:String
    },
    avatar_src:{
      type: String
    }
  },

  /**
   * 组件的初始数据
   */
  data: {

  },

  /**
   * 组件的方法列表
   */
  methods: {
    showtip: function (e) {
      wx.showModal({
        title: '预约提示',
        content: '是否预约这个角色',
        success: function (res) {
          if (res.confirm) {
            console.log('用户点击预约')
          }
          else {
            console.log('用户点击取消')
          }
        }
      })
    }
  },
})
