// pages/settings/settings.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    activity_message: {
      type: '每周会议',
      meeting_topic: '如何幽默演讲',
      meeting_time: '2019-02-15 19:00',
      meeting_location: '南京东路201弄',
      guest: 'Kelly',
      club: 'AmazingFriday'
    }
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

  onNavigateToActivity: function (event) {
    wx.switchTab({
      url: '/pages/activity/activity',
    })
  }
})