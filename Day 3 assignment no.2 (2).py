{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assignment No.2 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q.1. Use IF ELSE and ELIF to write a program in python for your Report Cards. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#if else & elif"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Distinction\n"
     ]
    }
   ],
   "source": [
    "marks = 80\n",
    "\n",
    "if marks >= 75:\n",
    "    print(\"Distinction\")\n",
    "elif marks >=60 and marks <=75:\n",
    "    print(\"First class\")\n",
    "elif marks >= 50 and marks < 60:\n",
    "    print(\"Second class\")\n",
    "else:\n",
    "    print(\"Failed\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q.2. Use For Loop to Print Prime Numbers in between 1 to 1000."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n",
      "21\n",
      "22\n",
      "23\n",
      "24\n",
      "25\n",
      "26\n",
      "27\n",
      "28\n",
      "29\n",
      "30\n",
      "31\n",
      "32\n",
      "33\n",
      "34\n",
      "35\n",
      "36\n",
      "37\n",
      "38\n",
      "39\n",
      "40\n",
      "41\n",
      "42\n",
      "43\n",
      "44\n",
      "45\n",
      "46\n",
      "47\n",
      "48\n",
      "49\n",
      "50\n",
      "51\n",
      "52\n",
      "53\n",
      "54\n",
      "55\n",
      "56\n",
      "57\n",
      "58\n",
      "59\n",
      "60\n",
      "61\n",
      "62\n",
      "63\n",
      "64\n",
      "65\n",
      "66\n",
      "67\n",
      "68\n",
      "69\n",
      "70\n",
      "71\n",
      "72\n",
      "73\n",
      "74\n",
      "75\n",
      "76\n",
      "77\n",
      "78\n",
      "79\n",
      "80\n",
      "81\n",
      "82\n",
      "83\n",
      "84\n",
      "85\n",
      "86\n",
      "87\n",
      "88\n",
      "89\n",
      "90\n",
      "91\n",
      "92\n",
      "93\n",
      "94\n",
      "95\n",
      "96\n",
      "97\n",
      "98\n",
      "99\n",
      "100\n",
      "101\n",
      "102\n",
      "103\n",
      "104\n",
      "105\n",
      "106\n",
      "107\n",
      "108\n",
      "109\n",
      "110\n",
      "111\n",
      "112\n",
      "113\n",
      "114\n",
      "115\n",
      "116\n",
      "117\n",
      "118\n",
      "119\n",
      "120\n",
      "121\n",
      "122\n",
      "123\n",
      "124\n",
      "125\n",
      "126\n",
      "127\n",
      "128\n",
      "129\n",
      "130\n",
      "131\n",
      "132\n",
      "133\n",
      "134\n",
      "135\n",
      "136\n",
      "137\n",
      "138\n",
      "139\n",
      "140\n",
      "141\n",
      "142\n",
      "143\n",
      "144\n",
      "145\n",
      "146\n",
      "147\n",
      "148\n",
      "149\n",
      "150\n",
      "151\n",
      "152\n",
      "153\n",
      "154\n",
      "155\n",
      "156\n",
      "157\n",
      "158\n",
      "159\n",
      "160\n",
      "161\n",
      "162\n",
      "163\n",
      "164\n",
      "165\n",
      "166\n",
      "167\n",
      "168\n",
      "169\n",
      "170\n",
      "171\n",
      "172\n",
      "173\n",
      "174\n",
      "175\n",
      "176\n",
      "177\n",
      "178\n",
      "179\n",
      "180\n",
      "181\n",
      "182\n",
      "183\n",
      "184\n",
      "185\n",
      "186\n",
      "187\n",
      "188\n",
      "189\n",
      "190\n",
      "191\n",
      "192\n",
      "193\n",
      "194\n",
      "195\n",
      "196\n",
      "197\n",
      "198\n",
      "199\n",
      "200\n",
      "201\n",
      "202\n",
      "203\n",
      "204\n",
      "205\n",
      "206\n",
      "207\n",
      "208\n",
      "209\n",
      "210\n",
      "211\n",
      "212\n",
      "213\n",
      "214\n",
      "215\n",
      "216\n",
      "217\n",
      "218\n",
      "219\n",
      "220\n",
      "221\n",
      "222\n",
      "223\n",
      "224\n",
      "225\n",
      "226\n",
      "227\n",
      "228\n",
      "229\n",
      "230\n",
      "231\n",
      "232\n",
      "233\n",
      "234\n",
      "235\n",
      "236\n",
      "237\n",
      "238\n",
      "239\n",
      "240\n",
      "241\n",
      "242\n",
      "243\n",
      "244\n",
      "245\n",
      "246\n",
      "247\n",
      "248\n",
      "249\n",
      "250\n",
      "251\n",
      "252\n",
      "253\n",
      "254\n",
      "255\n",
      "256\n",
      "257\n",
      "258\n",
      "259\n",
      "260\n",
      "261\n",
      "262\n",
      "263\n",
      "264\n",
      "265\n",
      "266\n",
      "267\n",
      "268\n",
      "269\n",
      "270\n",
      "271\n",
      "272\n",
      "273\n",
      "274\n",
      "275\n",
      "276\n",
      "277\n",
      "278\n",
      "279\n",
      "280\n",
      "281\n",
      "282\n",
      "283\n",
      "284\n",
      "285\n",
      "286\n",
      "287\n",
      "288\n",
      "289\n",
      "290\n",
      "291\n",
      "292\n",
      "293\n",
      "294\n",
      "295\n",
      "296\n",
      "297\n",
      "298\n",
      "299\n",
      "300\n",
      "301\n",
      "302\n",
      "303\n",
      "304\n",
      "305\n",
      "306\n",
      "307\n",
      "308\n",
      "309\n",
      "310\n",
      "311\n",
      "312\n",
      "313\n",
      "314\n",
      "315\n",
      "316\n",
      "317\n",
      "318\n",
      "319\n",
      "320\n",
      "321\n",
      "322\n",
      "323\n",
      "324\n",
      "325\n",
      "326\n",
      "327\n",
      "328\n",
      "329\n",
      "330\n",
      "331\n",
      "332\n",
      "333\n",
      "334\n",
      "335\n",
      "336\n",
      "337\n",
      "338\n",
      "339\n",
      "340\n",
      "341\n",
      "342\n",
      "343\n",
      "344\n",
      "345\n",
      "346\n",
      "347\n",
      "348\n",
      "349\n",
      "350\n",
      "351\n",
      "352\n",
      "353\n",
      "354\n",
      "355\n",
      "356\n",
      "357\n",
      "358\n",
      "359\n",
      "360\n",
      "361\n",
      "362\n",
      "363\n",
      "364\n",
      "365\n",
      "366\n",
      "367\n",
      "368\n",
      "369\n",
      "370\n",
      "371\n",
      "372\n",
      "373\n",
      "374\n",
      "375\n",
      "376\n",
      "377\n",
      "378\n",
      "379\n",
      "380\n",
      "381\n",
      "382\n",
      "383\n",
      "384\n",
      "385\n",
      "386\n",
      "387\n",
      "388\n",
      "389\n",
      "390\n",
      "391\n",
      "392\n",
      "393\n",
      "394\n",
      "395\n",
      "396\n",
      "397\n",
      "398\n",
      "399\n",
      "400\n",
      "401\n",
      "402\n",
      "403\n",
      "404\n",
      "405\n",
      "406\n",
      "407\n",
      "408\n",
      "409\n",
      "410\n",
      "411\n",
      "412\n",
      "413\n",
      "414\n",
      "415\n",
      "416\n",
      "417\n",
      "418\n",
      "419\n",
      "420\n",
      "421\n",
      "422\n",
      "423\n",
      "424\n",
      "425\n",
      "426\n",
      "427\n",
      "428\n",
      "429\n",
      "430\n",
      "431\n",
      "432\n",
      "433\n",
      "434\n",
      "435\n",
      "436\n",
      "437\n",
      "438\n",
      "439\n",
      "440\n",
      "441\n",
      "442\n",
      "443\n",
      "444\n",
      "445\n",
      "446\n",
      "447\n",
      "448\n",
      "449\n",
      "450\n",
      "451\n",
      "452\n",
      "453\n",
      "454\n",
      "455\n",
      "456\n",
      "457\n",
      "458\n",
      "459\n",
      "460\n",
      "461\n",
      "462\n",
      "463\n",
      "464\n",
      "465\n",
      "466\n",
      "467\n",
      "468\n",
      "469\n",
      "470\n",
      "471\n",
      "472\n",
      "473\n",
      "474\n",
      "475\n",
      "476\n",
      "477\n",
      "478\n",
      "479\n",
      "480\n",
      "481\n",
      "482\n",
      "483\n",
      "484\n",
      "485\n",
      "486\n",
      "487\n",
      "488\n",
      "489\n",
      "490\n",
      "491\n",
      "492\n",
      "493\n",
      "494\n",
      "495\n",
      "496\n",
      "497\n",
      "498\n",
      "499\n",
      "500\n",
      "501\n",
      "502\n",
      "503\n",
      "504\n",
      "505\n",
      "506\n",
      "507\n",
      "508\n",
      "509\n",
      "510\n",
      "511\n",
      "512\n",
      "513\n",
      "514\n",
      "515\n",
      "516\n",
      "517\n",
      "518\n",
      "519\n",
      "520\n",
      "521\n",
      "522\n",
      "523\n",
      "524\n",
      "525\n",
      "526\n",
      "527\n",
      "528\n",
      "529\n",
      "530\n",
      "531\n",
      "532\n",
      "533\n",
      "534\n",
      "535\n",
      "536\n",
      "537\n",
      "538\n",
      "539\n",
      "540\n",
      "541\n",
      "542\n",
      "543\n",
      "544\n",
      "545\n",
      "546\n",
      "547\n",
      "548\n",
      "549\n",
      "550\n",
      "551\n",
      "552\n",
      "553\n",
      "554\n",
      "555\n",
      "556\n",
      "557\n",
      "558\n",
      "559\n",
      "560\n",
      "561\n",
      "562\n",
      "563\n",
      "564\n",
      "565\n",
      "566\n",
      "567\n",
      "568\n",
      "569\n",
      "570\n",
      "571\n",
      "572\n",
      "573\n",
      "574\n",
      "575\n",
      "576\n",
      "577\n",
      "578\n",
      "579\n",
      "580\n",
      "581\n",
      "582\n",
      "583\n",
      "584\n",
      "585\n",
      "586\n",
      "587\n",
      "588\n",
      "589\n",
      "590\n",
      "591\n",
      "592\n",
      "593\n",
      "594\n",
      "595\n",
      "596\n",
      "597\n",
      "598\n",
      "599\n",
      "600\n",
      "601\n",
      "602\n",
      "603\n",
      "604\n",
      "605\n",
      "606\n",
      "607\n",
      "608\n",
      "609\n",
      "610\n",
      "611\n",
      "612\n",
      "613\n",
      "614\n",
      "615\n",
      "616\n",
      "617\n",
      "618\n",
      "619\n",
      "620\n",
      "621\n",
      "622\n",
      "623\n",
      "624\n",
      "625\n",
      "626\n",
      "627\n",
      "628\n",
      "629\n",
      "630\n",
      "631\n",
      "632\n",
      "633\n",
      "634\n",
      "635\n",
      "636\n",
      "637\n",
      "638\n",
      "639\n",
      "640\n",
      "641\n",
      "642\n",
      "643\n",
      "644\n",
      "645\n",
      "646\n",
      "647\n",
      "648\n",
      "649\n",
      "650\n",
      "651\n",
      "652\n",
      "653\n",
      "654\n",
      "655\n",
      "656\n",
      "657\n",
      "658\n",
      "659\n",
      "660\n",
      "661\n",
      "662\n",
      "663\n",
      "664\n",
      "665\n",
      "666\n",
      "667\n",
      "668\n",
      "669\n",
      "670\n",
      "671\n",
      "672\n",
      "673\n",
      "674\n",
      "675\n",
      "676\n",
      "677\n",
      "678\n",
      "679\n",
      "680\n",
      "681\n",
      "682\n",
      "683\n",
      "684\n",
      "685\n",
      "686\n",
      "687\n",
      "688\n",
      "689\n",
      "690\n",
      "691\n",
      "692\n",
      "693\n",
      "694\n",
      "695\n",
      "696\n",
      "697\n",
      "698\n",
      "699\n",
      "700\n",
      "701\n",
      "702\n",
      "703\n",
      "704\n",
      "705\n",
      "706\n",
      "707\n",
      "708\n",
      "709\n",
      "710\n",
      "711\n",
      "712\n",
      "713\n",
      "714\n",
      "715\n",
      "716\n",
      "717\n",
      "718\n",
      "719\n",
      "720\n",
      "721\n",
      "722\n",
      "723\n",
      "724\n",
      "725\n",
      "726\n",
      "727\n",
      "728\n",
      "729\n",
      "730\n",
      "731\n",
      "732\n",
      "733\n",
      "734\n",
      "735\n",
      "736\n",
      "737\n",
      "738\n",
      "739\n",
      "740\n",
      "741\n",
      "742\n",
      "743\n",
      "744\n",
      "745\n",
      "746\n",
      "747\n",
      "748\n",
      "749\n",
      "750\n",
      "751\n",
      "752\n",
      "753\n",
      "754\n",
      "755\n",
      "756\n",
      "757\n",
      "758\n",
      "759\n",
      "760\n",
      "761\n",
      "762\n",
      "763\n",
      "764\n",
      "765\n",
      "766\n",
      "767\n",
      "768\n",
      "769\n",
      "770\n",
      "771\n",
      "772\n",
      "773\n",
      "774\n",
      "775\n",
      "776\n",
      "777\n",
      "778\n",
      "779\n",
      "780\n",
      "781\n",
      "782\n",
      "783\n",
      "784\n",
      "785\n",
      "786\n",
      "787\n",
      "788\n",
      "789\n",
      "790\n",
      "791\n",
      "792\n",
      "793\n",
      "794\n",
      "795\n",
      "796\n",
      "797\n",
      "798\n",
      "799\n",
      "800\n",
      "801\n",
      "802\n",
      "803\n",
      "804\n",
      "805\n",
      "806\n",
      "807\n",
      "808\n",
      "809\n",
      "810\n",
      "811\n",
      "812\n",
      "813\n",
      "814\n",
      "815\n",
      "816\n",
      "817\n",
      "818\n",
      "819\n",
      "820\n",
      "821\n",
      "822\n",
      "823\n",
      "824\n",
      "825\n",
      "826\n",
      "827\n",
      "828\n",
      "829\n",
      "830\n",
      "831\n",
      "832\n",
      "833\n",
      "834\n",
      "835\n",
      "836\n",
      "837\n",
      "838\n",
      "839\n",
      "840\n",
      "841\n",
      "842\n",
      "843\n",
      "844\n",
      "845\n",
      "846\n",
      "847\n",
      "848\n",
      "849\n",
      "850\n",
      "851\n",
      "852\n",
      "853\n",
      "854\n",
      "855\n",
      "856\n",
      "857\n",
      "858\n",
      "859\n",
      "860\n",
      "861\n",
      "862\n",
      "863\n",
      "864\n",
      "865\n",
      "866\n",
      "867\n",
      "868\n",
      "869\n",
      "870\n",
      "871\n",
      "872\n",
      "873\n",
      "874\n",
      "875\n",
      "876\n",
      "877\n",
      "878\n",
      "879\n",
      "880\n",
      "881\n",
      "882\n",
      "883\n",
      "884\n",
      "885\n",
      "886\n",
      "887\n",
      "888\n",
      "889\n",
      "890\n",
      "891\n",
      "892\n",
      "893\n",
      "894\n",
      "895\n",
      "896\n",
      "897\n",
      "898\n",
      "899\n",
      "900\n",
      "901\n",
      "902\n",
      "903\n",
      "904\n",
      "905\n",
      "906\n",
      "907\n",
      "908\n",
      "909\n",
      "910\n",
      "911\n",
      "912\n",
      "913\n",
      "914\n",
      "915\n",
      "916\n",
      "917\n",
      "918\n",
      "919\n",
      "920\n",
      "921\n",
      "922\n",
      "923\n",
      "924\n",
      "925\n",
      "926\n",
      "927\n",
      "928\n",
      "929\n",
      "930\n",
      "931\n",
      "932\n",
      "933\n",
      "934\n",
      "935\n",
      "936\n",
      "937\n",
      "938\n",
      "939\n",
      "940\n",
      "941\n",
      "942\n",
      "943\n",
      "944\n",
      "945\n",
      "946\n",
      "947\n",
      "948\n",
      "949\n",
      "950\n",
      "951\n",
      "952\n",
      "953\n",
      "954\n",
      "955\n",
      "956\n",
      "957\n",
      "958\n",
      "959\n",
      "960\n",
      "961\n",
      "962\n",
      "963\n",
      "964\n",
      "965\n",
      "966\n",
      "967\n",
      "968\n",
      "969\n",
      "970\n",
      "971\n",
      "972\n",
      "973\n",
      "974\n",
      "975\n",
      "976\n",
      "977\n",
      "978\n",
      "979\n",
      "980\n",
      "981\n",
      "982\n",
      "983\n",
      "984\n",
      "985\n",
      "986\n",
      "987\n",
      "988\n",
      "989\n",
      "990\n",
      "991\n",
      "992\n",
      "993\n",
      "994\n",
      "995\n",
      "996\n",
      "997\n",
      "998\n",
      "999\n"
     ]
    }
   ],
   "source": [
    "for item in range(1,1000):\n",
    "    print(item)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Q.3. Write a program for printing the tables from 1,10 using Nested For Loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: 7\n",
      "Multiplication Table of 7\n",
      "7 X 1 = 7\n",
      "7 X 2 = 14\n",
      "7 X 3 = 21\n",
      "7 X 4 = 28\n",
      "7 X 5 = 35\n",
      "7 X 6 = 42\n",
      "7 X 7 = 49\n",
      "7 X 8 = 56\n",
      "7 X 9 = 63\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter the number: \"))\n",
    "\n",
    "print(\"Multiplication Table of\", num)\n",
    "for a in range(1, 10):\n",
    "   print(num,\"X\",a,\"=\",num * a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q.4.Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from the user. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n"
     ]
    }
   ],
   "source": [
    "x=0\n",
    "while x<100:\n",
    "    print(x)\n",
    "    x=x+2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
