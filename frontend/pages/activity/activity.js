// pages/health/health.js
// pages/mall/mall.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    activity_message1:{
      club_name: 'AmazingFridayTMC',
      meeting_time: '2019-01-25 19:00',
      meeting_location: '南京东路201弄',
      topic: '如何幽默演讲',
      guest: 'Kelly',
      book_right: true,
      poster_image: '/images/activity/amazingfriday@logo.jpg'
    },
    activity_message2:{
      club_name: 'LighthouseTMC',
      meeting_time: '2019-01-26 19:00',
      meeting_location: '南京东路201弄',
      topic: '人工智能技术趋势',
      guest: 'Stephen',
      book_right: false,
      poster_image: '/images/activity/lighthouse@logo.jpg'
    },
    activity_message3:{
      club_name: 'SiemensSTAR',
      meeting_time: '2019-01-24 19:00',
      meeting_location: '南京东路201弄',
      topic: '如何使用肢体语言',
      guest: 'Johnson',
      book_right: false,
      poster_image: '/images/activity/siemensstar@logo.jpg'
    },
    imgUrls:[
      '/images/activity/amazingfriday@meeting1.jpg',
      '/images/activity/amazingfriday@meeting2.jpg',
      '/images/activity/amazingfriday@meeting3.jpg',
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  onNavigateToRole:function(){
    wx.switchTab({
      url: '/pages/meeting/meeting',
    })
  }
})