#!/usr/bin/env python3
"""
Test script to verify ML module integration
Tests basic functionality of the ensemble model and feature extractors
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path

# Add ML module to path
sys.path.append(str(Path(__file__).parent / 'ml'))

def test_feature_extractors():
    """Test individual feature extractors"""
    print("Testing Feature Extractors...")
    
    try:
        from features.url_features import URLFeatureExtractor
        url_extractor = URLFeatureExtractor()
        
        test_url = "https://www.example.com/login?redirect=home"
        url_features = url_extractor.extract_features(test_url)
        print(f"✓ URL Feature Extractor: {len(url_features)} features extracted")
        
        from features.content_features import ContentAnalyzer
        content_analyzer = ContentAnalyzer()
        
        content_features = content_analyzer.analyze_content(test_url)
        print(f"✓ Content Analyzer: {len(content_features)} features extracted")
        
        from features.domain_features import DomainFeatureExtractor
        domain_extractor = DomainFeatureExtractor()
        
        domain_features = domain_extractor.extract_features("example.com")
        print(f"✓ Domain Feature Extractor: {len(domain_features)} features extracted")
        
        from features.visual_features import VisualFeatureExtractor
        visual_extractor = VisualFeatureExtractor()
        
        # Test with empty screenshot path (should return defaults)
        visual_features = visual_extractor.extract_features("", test_url)
        print(f"✓ Visual Feature Extractor: {len(visual_features)} features extracted")
        
        return True
        
    except Exception as e:
        print(f"✗ Feature Extractor Test Failed: {str(e)}")
        return False

def test_data_processing():
    """Test data processing modules"""
    print("\nTesting Data Processing...")
    
    try:
        from data.preprocessor import DataPreprocessor
        preprocessor = DataPreprocessor()
        
        # Create dummy data
        test_data = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [0.1, 0.2, 0.3, 0.4, 0.5],
            'feature3': [10, 20, 30, 40, 50]
        })
        
        preprocessor.fit(test_data)
        processed_data = preprocessor.transform(test_data)
        print(f"✓ Data Preprocessor: {processed_data.shape} output shape")
        
        from data.augmentation import DataAugmenter
        augmenter = DataAugmenter()
        
        test_labels = pd.Series([0, 1, 0, 1, 0])
        augmented_X, augmented_y = augmenter.augment_dataset(test_data, test_labels, 0.2)
        print(f"✓ Data Augmenter: {len(augmented_X)} samples after augmentation")
        
        return True
        
    except Exception as e:
        print(f"✗ Data Processing Test Failed: {str(e)}")
        return False

def test_ensemble_model():
    """Test ensemble model functionality"""
    print("\nTesting Ensemble Model...")
    
    try:
        from models.ensemble_model import PhishingEnsembleModel
        
        # Create ensemble model
        model = PhishingEnsembleModel()
        print("✓ Ensemble Model Initialized")
        
        # Create dummy training data
        np.random.seed(42)
        n_samples = 100
        n_features = 20
        
        # Generate random features
        X = pd.DataFrame(np.random.rand(n_samples, n_features), 
                        columns=[f'feature_{i}' for i in range(n_features)])
        y = pd.Series(np.random.randint(0, 2, n_samples))
        
        print(f"Training with {n_samples} samples and {n_features} features...")
        
        # Test fit method
        model.fit(X, y)
        print("✓ Model Training Completed")
        
        # Test predict method
        predictions = model.predict(X[:10])
        print(f"✓ Predictions: {predictions.shape}")
        
        # Test predict_proba method
        probabilities = model.predict_proba(X[:10])
        print(f"✓ Probabilities: {probabilities.shape}")
        
        # Test feature importance
        importance = model.get_feature_importance()
        print(f"✓ Feature Importance: {len(importance)} values")
        
        return True
        
    except Exception as e:
        print(f"✗ Ensemble Model Test Failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_utilities():
    """Test utility modules"""
    print("\nTesting Utilities...")
    
    try:
        from utils.metrics import PhishingMetrics
        metrics = PhishingMetrics()
        
        # Test metrics calculation
        y_true = np.array([0, 1, 0, 1, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        y_proba = np.array([0.1, 0.9, 0.2, 0.4, 0.8])
        
        all_metrics = metrics.calculate_all_metrics(y_true, y_pred, y_proba)
        print(f"✓ Metrics Calculation: {len(all_metrics)} metrics computed")
        
        from utils.ssl_checker import SSLChecker
        ssl_checker = SSLChecker()
        print("✓ SSL Checker Initialized")
        
        from utils.whois_lookup import WHOISAnalyzer
        whois_analyzer = WHOISAnalyzer()
        print("✓ WHOIS Analyzer Initialized")
        
        return True
        
    except Exception as e:
        print(f"✗ Utilities Test Failed: {str(e)}")
        return False

def test_training_pipeline():
    """Test training pipeline components"""
    print("\nTesting Training Pipeline...")
    
    try:
        from training.train import ModelTrainer
        from training.evaluate import ModelEvaluator
        from training.hyperparameter_tuning import HyperparameterTuner
        
        print("✓ Training Pipeline Components Imported")
        
        # Test basic initialization
        trainer = ModelTrainer()
        print("✓ Model Trainer Initialized")
        
        evaluator = ModelEvaluator()
        print("✓ Model Evaluator Initialized")
        
        tuner = HyperparameterTuner()
        print("✓ Hyperparameter Tuner Initialized")
        
        return True
        
    except Exception as e:
        print(f"✗ Training Pipeline Test Failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("=== ML Module Integration Test ===")
    print()
    
    test_results = []
    
    test_results.append(test_feature_extractors())
    test_results.append(test_data_processing())
    test_results.append(test_ensemble_model())
    test_results.append(test_utilities())
    test_results.append(test_training_pipeline())
    
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    
    passed = sum(test_results)
    total = len(test_results)
    
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {passed/total*100:.1f}%")
    
    if passed == total:
        print("\n🎉 All tests passed! ML module integration is working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Check the error messages above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)