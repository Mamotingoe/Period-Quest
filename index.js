import React, { useState } from 'react';
import { AlertCircle, Heart, Droplet, Smile, Calendar, Award, Gift } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Progress } from '@/components/ui/progress';

const PeriodQuest = () => {
  const [health, setHealth] = useState(80);
  const [hygiene, setHygiene] = useState(75);
  const [happiness, setHappiness] = useState(90);
  const [daysUntilPeriod, setDaysUntilPeriod] = useState(14);
  const [points, setPoints] = useState(50);
  const [vouchers, setVouchers] = useState(2);

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center text-purple-600">Period Quest</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <Card>
          <CardHeader>
            <CardTitle>Player Status</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center">
                <Heart className="mr-2 text-red-500" />
                <span className="mr-2">Health:</span>
                <Progress value={health} className="flex-grow" />
              </div>
              <div className="flex items-center">
                <Droplet className="mr-2 text-blue-500" />
                <span className="mr-2">Hygiene:</span>
                <Progress value={hygiene} className="flex-grow" />
              </div>
              <div className="flex items-center">
                <Smile className="mr-2 text-yellow-500" />
                <span className="mr-2">Happiness:</span>
                <Progress value={happiness} className="flex-grow" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Game Stats</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center">
                <Calendar className="mr-2 text-green-500" />
                <span>Days until next period: {daysUntilPeriod}</span>
              </div>
              <div className="flex items-center">
                <Award className="mr-2 text-purple-500" />
                <span>Points: {points}</span>
              </div>
              <div className="flex items-center">
                <Gift className="mr-2 text-pink-500" />
                <span>Vouchers: {vouchers}</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Alert>
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Heads up!</AlertTitle>
        <AlertDescription>
          Your period is coming up in {daysUntilPeriod} days. Make sure you're prepared!
        </AlertDescription>
      </Alert>

      <div className="mt-6">
        <h2 className="text-xl font-semibold mb-3">Available Quests</h2>
        <div className="space-y-3">
          {['Hygiene Quest', 'Wellness Quest', 'Advocacy Quest'].map((quest, index) => (
            <Card key={index}>
              <CardHeader>
                <CardTitle>{quest}</CardTitle>
              </CardHeader>
              <CardContent>
                <p>Complete this quest to earn points and improve your stats!</p>
                <button className="mt-2 px-4 py-2 bg-purple-500 text-white rounded hover:bg-purple-600 transition-colors">
                  Start Quest
                </button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PeriodQuest;