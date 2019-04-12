import React from 'react';
import { Image } from 'react-native';
import { createBottomTabNavigator,  createAppContainer, createStackNavigator } from 'react-navigation';

import Leaderboard from './Leaderboard';
import Quiz from './Quiz';
import Profile from './Profile';

const leaderImg = require('./Resources/Images/leaderboard.png');
const quizImg = require('./Resources/Images/quiz.png');
const profImg = require('./Resources/Images/user.png');

const TabNavi = createBottomTabNavigator({
    leaderboard: {
        screen: Leaderboard,
        navigationOptions: {
        tabBarIcon: ({ focused }) => (
            focused ? 
            <Image source={leaderImg} style={{width:35, height:35, tintColor:'#fff'}} /> 
            : 
            <Image source={leaderImg} style={{width:25, height:25}} />)
        },
    },
    quiz: {
        screen: Quiz,
        navigationOptions: {
            tabBarIcon: ({ focused }) => (
                focused ? 
                <Image source={quizImg} style={{width:35, height:35, tintColor:'#fff'}} /> 
                : 
                <Image source={quizImg} style={{width:25, height:25}} />)
        },
    },
    profile: {
        screen: Profile,
        navigationOptions: {
            tabBarIcon: ({ focused }) => (
                focused ? 
                <Image source={profImg} style={{width:35, height:35, tintColor:'#fff'}} /> 
                : 
                <Image source={profImg} style={{width:25, height:25}} />)
        },
    },
  },{
    tabBarOptions: {
      header: null,
      showIcon: true,
      showLabel: false,
      style: {
          height:50,
        backgroundColor: '#4CAF50'
      },
    }
  }); 


export default createAppContainer(TabNavi);