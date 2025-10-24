#!/usr/bin/env python3
"""
AegisLab Advanced Threat Hunting Demo
=====================================

This script demonstrates the advanced machine learning capabilities
from the Jupyter notebook in a standalone format.
"""

import sys
import os
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

try:
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import IsolationForest
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    import re
    from datetime import datetime
    import warnings
    warnings.filterwarnings('ignore')
    
    print("🛡️ AegisLab Advanced Threat Hunting Demo")
    print("=" * 50)
    print("🔬 Machine Learning-Based Cybersecurity Analytics")
    print(f"📅 Analysis Runtime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Demonstrate the advanced analytics capabilities
    class AdvancedThreatDemo:
        def __init__(self):
            self.scaler = StandardScaler()
            self.isolation_forest = IsolationForest(contamination=0.1, random_state=42)
            
        def demonstrate_capabilities(self):
            """Showcase advanced threat hunting capabilities"""
            
            print("🎯 Advanced Analytics Capabilities:")
            print("   ✅ Statistical Anomaly Detection (Isolation Forest, Z-score, IQR)")
            print("   ✅ Behavioral Clustering (DBSCAN with PCA optimization)")
            print("   ✅ Feature Engineering for Cybersecurity Datasets")
            print("   ✅ MITRE ATT&CK Framework Integration")
            print("   ✅ Custom Threat Scoring Algorithms")
            print("   ✅ Advanced Visualization & Executive Reporting")
            print()
            
            # Generate sample data to demonstrate concepts
            print("📊 Generating Synthetic Threat Data for Demo...")
            sample_data = self._generate_sample_threat_data()
            
            print(f"🔍 Analyzing {len(sample_data)} simulated IP addresses")
            
            # Demonstrate anomaly detection
            features = ['request_count', 'error_rate', 'failed_logins', 'path_diversity']
            X = sample_data[features]
            X_scaled = self.scaler.fit_transform(X)
            
            # Run isolation forest
            anomalies = self.isolation_forest.fit_predict(X_scaled)
            anomaly_scores = self.isolation_forest.decision_function(X_scaled)
            
            anomalous_count = (anomalies == -1).sum()
            print(f"🚨 Detected {anomalous_count} anomalous entities ({anomalous_count/len(sample_data):.1%})")
            
            # Demonstrate clustering
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X_scaled)
            
            dbscan = DBSCAN(eps=0.5, min_samples=3)
            clusters = dbscan.fit_predict(X_pca)
            
            n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
            print(f"🔗 Identified {n_clusters} distinct behavioral clusters")
            
            # Demonstrate MITRE ATT&CK mapping
            attack_techniques = self._map_to_attack_framework(sample_data)
            print(f"🎖️ Mapped behaviors to {len(attack_techniques)} MITRE ATT&CK techniques")
            
            # Show top threats
            sample_data['anomaly_score'] = np.abs(anomaly_scores) * 100
            sample_data['cluster'] = clusters
            
            top_threats = sample_data.nlargest(3, 'anomaly_score')
            print(f"\\n🔥 Top 3 Threat Entities:")
            for i, (_, row) in enumerate(top_threats.iterrows(), 1):
                print(f"   {i}. IP {row['ip']} | Score: {row['anomaly_score']:.1f} | "
                      f"Failed Logins: {row['failed_logins']} | Error Rate: {row['error_rate']:.1%}")
            
            print(f"\\n✅ Advanced threat hunting analysis complete!")
            print(f"📈 This demonstrates enterprise-grade cybersecurity data science capabilities")
            
        def _generate_sample_threat_data(self):
            """Generate realistic synthetic threat data for demonstration"""
            np.random.seed(42)
            n_ips = 50
            
            data = {
                'ip': [f"192.168.1.{i}" for i in range(1, n_ips + 1)],
                'request_count': np.random.lognormal(3, 1, n_ips).astype(int),
                'error_rate': np.random.beta(2, 8, n_ips),
                'failed_logins': np.random.poisson(3, n_ips),
                'path_diversity': np.random.poisson(10, n_ips),
                'suspicious_paths': np.random.poisson(1, n_ips)
            }
            
            # Add some clear anomalies
            data['request_count'][:5] = np.random.randint(200, 500, 5)  # High volume
            data['failed_logins'][:3] = np.random.randint(20, 50, 3)   # Brute force
            data['error_rate'][:2] = np.random.uniform(0.6, 0.9, 2)    # High errors
            
            return pd.DataFrame(data)
        
        def _map_to_attack_framework(self, df):
            """Demonstrate MITRE ATT&CK mapping"""
            techniques = set()
            
            for _, row in df.iterrows():
                if row['failed_logins'] > 10:
                    techniques.add('T1110 - Brute Force')
                if row['path_diversity'] > 20:
                    techniques.add('T1083 - File and Directory Discovery')
                if row['error_rate'] > 0.5:
                    techniques.add('T1595 - Active Scanning')
                if row['request_count'] > 100:
                    techniques.add('T1046 - Network Service Scanning')
            
            return techniques
    
    # Run the demonstration
    demo = AdvancedThreatDemo()
    demo.demonstrate_capabilities()
    
    print(f"\\n🎓 Educational Note:")
    print(f"   This demonstration showcases advanced cybersecurity data science")
    print(f"   techniques that would typically require specialized expertise in:")
    print(f"   • Machine Learning & Statistical Analysis")
    print(f"   • Cybersecurity Domain Knowledge") 
    print(f"   • MITRE ATT&CK Framework")
    print(f"   • Advanced Python Programming")
    print(f"\\n📚 For full interactive analysis, see: analysis/advanced_threat_hunting.ipynb")

except ImportError as e:
    print(f"⚠️ Missing dependencies for advanced analytics: {e}")
    print(f"📦 Install with: pip install -r tools/requirements.txt")
    print(f"💡 This demonstrates sophisticated ML capabilities when dependencies are available")