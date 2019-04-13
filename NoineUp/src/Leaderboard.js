import React , {Component} from 'react';
import { View, Text, ScrollView } from 'react-native';
import firebase from 'firebase';

export default class Leaderboard extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }
      state = {leaders:[], names:[], noDisplay:false}


        
        
      componentDidMount()
      {
          var p = this.state.leaders
          var q = this.state.names
        firebase.database().ref('users').on('value', (users)=>{
                    users.forEach(element => {
                        this.setState({leaders:[ ...this.state.leaders,element.val().ablLevel], names:[...this.state.names, element.val().username]})
                    });
        }, ()=>{
            firebase.database().ref(`users/${firebase.auth().currentUser.uid}`).on('value',(use)=>
        {   
            console.log("asdadadasfdadv",use.val())
            if(use.val().category=="User")
                this.setState({noDisplay:true})
        })
        });

        
        console.log("arrr",typeof this.state.leaders,this.state.names)
      }

    
    swap(arr, first_Index, second_Index){
        var temp = arr[first_Index];
        arr[first_Index] = arr[second_Index];
        arr[second_Index] = temp;
    }
    
    bubble_Sort(arr,names){
    
        var len = arr.length,
            i, j, stop;
    
        for (i=0; i < len; i++){
            for (j=0, stop=len-i; j < stop; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                    swap(names, j, j+1);
                }
            }
        }
    
        return [arr,names];
    }


      displayLeaders()
      {
          if(!this.state.noDisplay)
          {
            var arr =[ ...this.state.leaders]
            var names = [ ...this.state.names]
            console.log(arr)
            var items = []

            var k = 0;

            if(this.state.leaders!=null)
            { 
                console.log(arr.length)
            var len = this.state.leaders.length,
            i, j, stop;
    
        for (i=0; i < len; i++){
            for (j=0, stop=len-i; j < stop; j++){
                if (arr[j] < arr[j+1]){
                    this.swap(arr, j, j+1);
                    this.swap(names, j, j+1);
                }
            }
        }

            for(k=0;k<arr.length;k++)
            {
    
                    items.push(<View style={{flexDirection:'row', width:'100%', height:60, backgroundColor:'#E0E0E0', marginBottom:5, alignItems:'center', justifyContent:'space-around'}}>
                                <Text style={{fontSize:20, color:'black'}}>{names[k]}</Text>
                                <Text style={{fontSize:20, color:'black'}}>{arr[k]*100}</Text>
                                </View>)
                
            }
        }

            return items
    }

    else
    {
        return <View style={{marginTop:150,width:'100%',alignItems:'center'}}><Text style={{color:'#fff', fontSize:24}}>Not available for Users</Text></View>
    }


      }

    render()
    {   console.log(this.state)
        return(
            <ScrollView style={{backgroundColor:'#0a1a29'}}>
                <View style={{top:0,left:0,right:0, height:50, backgroundColor:'#4CAF50', alignItems:'center', justifyContent:'center'}}>
                    <Text style={{color:'#fff', fontSize:18}}>LeaderBoard</Text>
                </View>
                {this.displayLeaders()}
            </ScrollView>
        )
    }

}