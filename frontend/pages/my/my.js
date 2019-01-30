import { 
  promisic 
} from '../../utils/common'

import {
  UserModel
} from '../../models/user'

const userModel = new UserModel()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentData: 0,
    activity_message: {
      type: 'AmazingFridayTMC 日常会议',
      meeting_topic: '如何幽默演讲',
      meeting_time: '2019-02-15 19:00',
      meeting_location: '南京东路201弄',
      guest: 'Kelly',
    },
    book_message:{
      type:'AmazingFridayTMC 日常会议',
      meeting_time: '2019-01-25 19:00',
      meeting_location: '南京东路201弄',
      role: 'Speaker',
      meeting_topic: '如何幽默演讲'
    },
    club_message: {
      club_name: 'AmazingFridayTMC',
      club_level: 'PathwayTwo',
      role: 'President',
      role_duty: 'Host a speech',
      mentor: 'Kelly'
    },
    authorized:false,
    userInfo: null,
    is_admin: true,
    is_login: true
  },

  onLoad: function (options) {
    // this.userLogin()
    this.userAuthoried()
    this.getUserInteractInfo()
  },

  getUserInteractInfo(){
    const _this = this
    userModel.getUserInteract()
    .then(data => {
      // console.log(data.interact)
      if(!data){
        return
      }
      console.log('before setData', _this.data.interact)
      this.setData({
        interact:data.interact
      })
      console.log('after setData', _this.data.interact)
    })
  },

  userLogin(){
    promisic(wx.login)()
    .then(data =>{
      if(data.code){
        userModel.getOpenId({
          code:data.code
        })
        .then(data => {
          console.log(data)
        })
      }
    })
  },

  userAuthoried(){
    promisic(wx.getSetting)()
    .then(data => {
      if(data.authSetting['scope.userInfo']){
        return promisic(wx.getUserInfo)()
      }
      return false
    })
    .then(data => {
      if(!data) {
        return
      }
      this.setData({
        authorized:true,
        userInfo:data.userInfo
      })
    })
  },

  userAuthoried_old(){
    wx.getSetting({
      success:data=>{
        if(data.authSetting['scope.userInfo']){
          wx.getUserInfo({
            success:data=>{
              this.setData({
                authorized:true,
                userInfo:data.userInfo
              })
            }
          })
        }
      }
    })
  },

  onGetUserInfo(event) {
    const userInfo = event.detail.userInfo
    if (userInfo) {
      console.log(userInfo)
      this.setData({
        userInfo:userInfo,
        authorized: true
      })
      userModel.postUserBaseinfo({
        'errorCode': 0,
        'msg': userInfo
      }).then(data=>{
        console.log(data)
      })
    }
  },

  //获取当前滑块的index
  bindchange: function (event) {
    // const that = this;
    this.setData({
      currentData: event.detail.current
    })
  },

  //点击切换，滑块index赋值
  checkCurrent: function (event) {
    // const that = this;
    var current_data = {}
    current_data = event.target.dataset.current;
    if (this.data.currentData === current_data) {
      return false;
    } 
    else {
      this.setData({
        currentData: current_data
      })  
    }
  },

  onNavigateToPublish: function(event){
    wx.navigateTo({
      url: '/pages/publish/publish',
    })
  },
  onNavigateToUserEdit: function (event) {
    wx.navigateTo({
      url: '/pages/user/user',
    })
  }
})