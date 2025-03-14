from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    services = {
        'healthcare': [
            {
                'title': 'Brain Tumor Detection',
                'description': 'Advanced AI-powered detection system for early diagnosis of brain tumors',
                'image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56',  # Brain MRI scan
                'icon': 'fa-brain'
            },
            {
                'title': 'Heart Disease Prediction',
                'description': 'ML-based prediction system for cardiovascular health assessment',
                'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d',  # ECG/heart monitor
                'icon': 'fa-heartbeat'
            },
            {
                'title': 'Telemedicine Platform',
                'description': 'Virtual healthcare consultations and remote patient monitoring',
                'image': 'https://images.unsplash.com/photo-1576091160550-2173dba999ef',  # Doctor video consultation
                'icon': 'fa-user-doctor'
            },
            {
                'title': 'Mood Tracking',
                'description': 'AI-powered mental health monitoring and support system',
                'image': 'https://images.unsplash.com/photo-1512676142074-50914091e423',  # Mental health visualization
                'icon': 'fa-face-smile'
            },
            {
                'title': 'Fitness Tracking',
                'description': 'Advanced workout monitoring and personalized fitness recommendations',
                'image': 'https://images.unsplash.com/photo-1510017803434-a899398421b3',  # Fitness tracking device
                'icon': 'fa-dumbbell'
            },
            {
                'title': 'Nutrition Planning',
                'description': 'AI-powered diet planning and nutritional analysis',
                'image': 'https://images.unsplash.com/photo-1543364195-bfe6e4932397',  # Healthy meal planning
                'icon': 'fa-apple-whole'
            },
            {
                'title': 'Medical Records',
                'description': 'Secure digital health record management system',
                'image': 'https://images.unsplash.com/photo-1587854692152-cbe660dbde88',  # Electronic health records
                'icon': 'fa-file-medical'
            }
        ],
        'agriculture': [
            {
                'title': 'Weather Analysis',
                'description': 'Advanced agricultural weather forecasting and analysis',
                'image': 'https://images.unsplash.com/photo-1504797798770-c5b9b4a3b6c5',  # Weather station
                'icon': 'fa-cloud-sun-rain'
            },
            {
                'title': 'Crop Monitoring',
                'description': 'AI-powered crop health and growth monitoring system',
                'image': 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0',  # Drone monitoring crops
                'icon': 'fa-seedling'
            },
            {
                'title': 'Disease Detection',
                'description': 'Early plant disease detection and treatment recommendations',
                'image': 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0',  # Infected plant analysis
                'icon': 'fa-virus'
            },
            {
                'title': 'Forest Protection',
                'description': 'Forest fire prediction and prevention system',
                'image': 'https://images.unsplash.com/photo-1547683905-f686c993c794',  # Forest monitoring system
                'icon': 'fa-tree'
            },
            {
                'title': 'Carbon Footprint',
                'description': 'Agricultural carbon emissions analysis and reduction',
                'image': 'https://images.unsplash.com/photo-1532601224476-15c79f2f7a51',  # Emissions monitoring
                'icon': 'fa-leaf'
            },
            {
                'title': 'Air Quality',
                'description': 'Real-time air pollution monitoring and analysis',
                'image': 'https://images.unsplash.com/photo-1584467541268-b040f83be3fd',  # Air quality station
                'icon': 'fa-wind'
            },
            {
                'title': 'Waste Management',
                'description': 'Smart agricultural waste recycling and management',
                'image': 'https://images.unsplash.com/photo-1532996122724-e3c354a0b15b',  # Modern recycling facility
                'icon': 'fa-recycle'
            }
        ],
        'entertainment': [
            {
                'title': 'Games Center',
                'description': 'AI-powered gaming hub with intelligent NPCs',
                'image': 'https://images.unsplash.com/photo-1552820728-8b83bb6b773f',  # Gaming setup
                'icon': 'fa-gamepad'
            },
            {
                'title': 'News Hub',
                'description': 'Personalized global news aggregation and analysis',
                'image': 'https://images.unsplash.com/photo-1495020689067-958852a7765e',  # Digital news
                'icon': 'fa-newspaper'
            },
            {
                'title': 'Meme Generator',
                'description': 'AI-powered meme and GIF creation tool',
                'image': 'https://images.unsplash.com/photo-1531259683007-016a7b628fc3',  # Meme creation
                'icon': 'fa-face-grin-tears'
            },
            {
                'title': 'Media Streaming',
                'description': 'Smart movie and music recommendations',
                'image': 'https://images.unsplash.com/photo-1516280440614-37939bbacd81',  # Streaming service
                'icon': 'fa-film'
            },
            {
                'title': 'AI Studio',
                'description': 'AI-powered photo and video generation',
                'image': 'https://images.unsplash.com/photo-1561883088-039e53143d73',  # AI image generation
                'icon': 'fa-camera'
            },
            {
                'title': 'Digital Audio',
                'description': 'Online music production and audio processing',
                'image': 'https://images.unsplash.com/photo-1598488035139-bdbb2231ce04',  # Digital audio workstation
                'icon': 'fa-music'
            }
        ],
        'research': [
            {
                'title': 'Cell Analysis',
                'description': 'Automated cell counting and analysis system',
                'image': 'https://images.unsplash.com/photo-1532187863486-abf9dbad1b69',  # Cell microscopy
                'icon': 'fa-microscope'
            },
            {
                'title': 'Tissue Biology',
                'description': 'Advanced tissue sample analysis platform',
                'image': 'https://images.unsplash.com/photo-1576086213369-97a306d36557',  # Tissue analysis
                'icon': 'fa-dna'
            },
            {
                'title': 'Nutrition Scanner',
                'description': 'Food composition and nutritional analysis',
                'image': 'https://images.unsplash.com/photo-1576086213149-c1b37280f3c7',  # Food analysis
                'icon': 'fa-utensils'
            }
        ],
        'space': [
            {
                'title': 'Cosmo Vision',
                'description': 'Advanced space observation and analysis',
                'image': 'https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45',  # Observatory
                'icon': 'fa-satellite'
            },
            {
                'title': 'Star Finder',
                'description': 'AI-powered constellation identification',
                'image': 'https://images.unsplash.com/photo-1419242902214-272b3f66ee7a',  # Star constellation
                'icon': 'fa-star'
            },
            {
                'title': 'Space Explorer',
                'description': 'Interactive space simulation and exploration',
                'image': 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa',  # Space simulation
                'icon': 'fa-rocket'
            },
            {
                'title': 'Planet Tracker',
                'description': 'Real-time planetary position monitoring',
                'image': 'https://images.unsplash.com/photo-1614642264762-147d089e6a70',  # Planet tracking
                'icon': 'fa-earth-americas'
            }
        ],
        'financial': [
            {
                'title': 'Investment AI',
                'description': 'AI-powered stock trading analysis and predictions',
                'image': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3',  # Stock trading
                'icon': 'fa-chart-line'
            },
            {
                'title': 'Crypto Advisor',
                'description': 'Cryptocurrency market analysis and predictions',
                'image': 'https://images.unsplash.com/photo-1621761191319-c6fb62004040',  # Crypto trading
                'icon': 'fa-bitcoin-sign'
            },
            {
                'title': 'DeFi Learning',
                'description': 'Decentralized finance education platform',
                'image': 'https://images.unsplash.com/photo-1639322537228-f710d846310a',  # DeFi education
                'icon': 'fa-graduation-cap'
            }
        ],
        'security': [
            {
                'title': 'VPN Service',
                'description': 'Secure VPN and proxy network solutions',
                'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb',  # Network security
                'icon': 'fa-shield-halved'
            },
            {
                'title': 'Password Manager',
                'description': 'Secure password storage and generation',
                'image': 'https://images.unsplash.com/photo-1614064641938-3bbee52942c7',  # Password security
                'icon': 'fa-key'
            },
            {
                'title': 'Security Guide',
                'description': 'Digital security education and updates',
                'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3',  # Security education
                'icon': 'fa-book'
            },
            {
                'title': 'Virus Guard',
                'description': 'Advanced malware detection and protection',
                'image': 'https://images.unsplash.com/photo-1563986768494-4dee9056b3c5',  # Antivirus protection
                'icon': 'fa-virus-slash'
            }
        ],
        'travel': [
            {
                'title': 'Smart Navigation',
                'description': 'AI-powered travel route optimization',
                'image': 'https://images.unsplash.com/photo-1502920514313-52581002a659',  # Navigation system
                'icon': 'fa-map-location-dot'
            },
            {
                'title': 'Vehicle Finder',
                'description': 'Nearby vehicle rental location services',
                'image': 'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2',  # Car rental
                'icon': 'fa-car'
            },
            {
                'title': 'Hotel Discovery',
                'description': 'AI-powered hotel recommendations and booking',
                'image': 'https://images.unsplash.com/photo-1566073771259-6a8506099945',  # Hotel booking
                'icon': 'fa-hotel'
            },
            {
                'title': 'Tour Planner',
                'description': 'Personalized travel itinerary planning',
                'image': 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800',  # Travel planning
                'icon': 'fa-plane'
            }
        ],
        'government': [
            {
                'title': 'PolicyGyan',
                'description': 'Rural policy information and guidance system',
                'image': 'https://images.unsplash.com/photo-1589578527966-fdac0f44566c',  # Rural development
                'icon': 'fa-landmark'
            },
            {
                'title': 'Politics Analysis',
                'description': 'Political trends and analysis platform',
                'image': 'https://images.unsplash.com/photo-1529107386315-e1a2ed48a620',  # Political analysis
                'icon': 'fa-scale-balanced'
            }
        ],
        'sports': [
            {
                'title': 'Live Scores',
                'description': 'Real-time sports scores and updates',
                'image': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',  # Live scoreboard
                'icon': 'fa-stopwatch'
            },
            {
                'title': 'AI Coach',
                'description': 'Personalized sports training and analysis',
                'image': 'https://images.unsplash.com/photo-1526506118085-60ce8714f8c5',  # Sports training
                'icon': 'fa-person-running'
            }
        ],
        'education': [
            {
                'title': 'BioLab Sim',
                'description': 'Virtual biology laboratory simulations',
                'image': 'https://images.unsplash.com/photo-1532187863486-abf9dbad1b69',  # Virtual lab
                'icon': 'fa-flask'
            },
            {
                'title': 'Circuit Lab',
                'description': 'Interactive electronics and Arduino simulations',
                'image': 'https://images.unsplash.com/photo-1554475901-4538ddfbccc2',  # Electronics lab
                'icon': 'fa-microchip'
            },
            {
                'title': 'ChemAI Tutor',
                'description': 'Chemistry learning and problem-solving AI',
                'image': 'https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6',  # Chemistry lab
                'icon': 'fa-atom'
            },
            {
                'title': 'MathAI Tutor',
                'description': 'Mathematics learning and problem-solving AI',
                'image': 'https://images.unsplash.com/photo-1635372722656-389f87a941b7',  # Math learning
                'icon': 'fa-calculator'
            }
        ]
    }
    return render_template('index.html', services=services)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)