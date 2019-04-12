import React , {Component} from 'react';
import { View, Text } from 'react-native';

export default class Profile extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }
    render()
    {
        return(
            <View>
                <Text>Profile</Text>
            </View>
        )
    }

}