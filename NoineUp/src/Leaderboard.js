import React , {Component} from 'react';
import { View, Text } from 'react-native';

export default class Leaderboard extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }
    render()
    {
        return(
            <View>
                <Text>Leaderboard</Text>
            </View>
        )
    }

}